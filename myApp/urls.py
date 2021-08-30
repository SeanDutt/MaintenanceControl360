from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('projects/', views.projects, name = 'projects'),
    path('testimonials/', views.testimonials, name = 'testimonials'),
    path('contact/', views.contact, name = 'contact'),
    path('projects/<int:pk>/', views.gallery_view, name="index"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)