from rest_framework import viewsets, permissions
from .models import Pattern, Comment
from .serializers import PatternSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

def register_view(request):
    return render(request, 'crochet/register.html')

@csrf_exempt
def api_register(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            if not username or not password:
                return JsonResponse({"error": "Username and password required."}, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Username already exists."}, status=400)

            user = User.objects.create_user(username=username, email=email, password=password)
            return JsonResponse({"message": "User created successfully.", "user": user.username}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)

    return JsonResponse({"error": "Only POST method allowed."}, status=405)


@csrf_exempt
def api_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({"message": "Login successful.", "auth_token": token.key})
        else:
            return JsonResponse({"error": "Invalid credentials."}, status=400)
    return JsonResponse({"error": "Only POST method allowed."}, status=405)

@csrf_exempt
def api_logout(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"message": "Logged out successfully."})
    return JsonResponse({"error": "Only POST method allowed."}, status=405)
   

class PatternViewSet(viewsets.ModelViewSet):
    queryset = Pattern.objects.all().order_by('-created_at')
    serializer_class = PatternSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

def patterns_list(request):
    patterns = Pattern.objects.select_related('user').prefetch_related('comments')[:100]
    return render(request, "crochet/patterns_list.html", {"patterns": patterns})

def pattern_detail(request, pk):
    pattern = get_object_or_404(Pattern.objects.prefetch_related('required_materials__material','used_stitches__stitch_type','comments__author'), pk=pk)
    return render(request, "crochet/pattern_detail.html", {"pattern": pattern})

def pattern_list_view(request):
    return render(request, 'crochet/pattern_list.html')

@login_required
def add_comment(request, pk):
    pattern = get_object_or_404(Pattern, pk=pk)
    if request.method == "POST":
        content = request.POST.get("content", "").strip()
        if content:
            Comment.objects.create(pattern=pattern, author=request.user, content=content)
    return redirect('pattern_detail', pk=pk)