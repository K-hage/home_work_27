from django.contrib import admin
from django.urls import path

from ads import views
from ads.views import AdListCreateView, CategoryListCreateView, AdDetailView, CategoryDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.root),
    path('cat/', CategoryListCreateView.as_view()),
    path('ad/', AdListCreateView.as_view()),
    path('cat/<int:pk>/', CategoryDetailView.as_view()),
    path('ad/<int:pk>/',  AdDetailView.as_view()),
]
