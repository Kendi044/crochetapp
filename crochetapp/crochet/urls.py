from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatternViewSet
from . import views


router = DefaultRouter()
router.register(r'patterns', PatternViewSet, basename='pattern')

urlpatterns = [
    path('patterns/<int:pk>/', views.pattern_detail, name='pattern_detail'),
    path('patterns/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('patterns/', views.pattern_list_view, name='pattern_list'),
    path('register/', views.register_view, name='register'),  # ✅ matches your view
    path('api/register/', views.api_register, name='api_register'),
    path('api/login/', views.api_login, name='api_login'),
    path('api/logout/', views.api_logout, name='api_logout'),
    path('api/', include(router.urls)),
]
