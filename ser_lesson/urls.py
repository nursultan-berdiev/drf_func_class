from django.contrib import admin
from django.urls import path
from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.genre_view),
    path('book/', views.BookView.as_view()),
    path('<int:pk>/', views.genre_detail),
    path('book/<int:pk>/', views.BookDetailView.as_view()),
]
