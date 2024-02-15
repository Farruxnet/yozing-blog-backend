from django.urls import path

from users.views.login import LoginView
from users.views.my_posts import MyPostsView, MyPostDetailView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('my-posts/', MyPostsView.as_view(), name='my-posts'),
    path('my-post-detail/<int:pk>', MyPostDetailView.as_view(), name='my-post-detail')
]
