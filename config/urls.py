from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from utils.views import core as core_views  # adjust path if needed

# DRF router setup
router = DefaultRouter()
router.register(r'users', core_views.UserViewSet)
router.register(r'clients', core_views.ClientProfileViewSet)
router.register(r'caregivers', core_views.CaregiverProfileViewSet)
router.register(r'jobs', core_views.JobViewSet)
router.register(r'payments', core_views.PaymentViewSet)
router.register(r'reviews', core_views.ReviewViewSet)
router.register(r'messages', core_views.MessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT auth endpoints from rest_framework_simplejwt
    path('api/', include('users.urls')),

    # Your DRF ViewSets
    path('api/', include(router.urls)),

    # Add other app-specific URLs if needed
    # path('api/someapp/', include('someapp.urls')),
]