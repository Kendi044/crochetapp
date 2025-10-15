from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# This is a simple Django view (not a REST API view) 
# designed to serve the main HTML file.
@api_view(['GET'])
@permission_classes([AllowAny])
def index(request):
    """
    Renders the main index.html template for the frontend application.
    """
    return render(request, 'crochet/index.html')
