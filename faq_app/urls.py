from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet, faq_list
from . import views


router = DefaultRouter()
router.register(r'faqs', FAQViewSet)

urlpatterns = [
    path('faqs/', faq_list, name='faq_list'),  # Maps URL to FAQ list view
    path('api/', include(router.urls)),  # API endpoints handled by DRF router
]