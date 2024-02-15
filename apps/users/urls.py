from django.urls import path

from users.views.login import LoginView
from users.views.my_posts import MyPostsView, MyPostDetailView
from users.views.user_detail import UserDetailView, UserMeDetailView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('detail/me/', UserMeDetailView.as_view(), name='me'),
    path('my-posts/', MyPostsView.as_view(), name='my-posts'),
    path('my-post-detail/<int:pk>', MyPostDetailView.as_view(), name='my-post-detail')
]
