from django.urls import path

from users.views.login import LoginView
from users.views.my_posts import MyPostsView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('my-posts/', MyPostsView.as_view(), name='my-posts')
]
