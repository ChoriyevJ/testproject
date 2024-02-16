from django.urls import path


from blog import views


urlpatterns = [
    path('posts/', views.PostListAPIView.as_view()),
    path('categories/', views.CategoryListAPIView.as_view())
]



