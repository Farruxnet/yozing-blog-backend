from django.urls import path

from yozing.views.create_yozing import YozingCreateView
from yozing.views.delete_yozing import YozingDeleteView
from yozing.views.detail_yozing import YozingDetailView
from yozing.views.list_yozing import YozingListView
from yozing.views.update_yozing import YozingUpdateView
from yozing.views.users_posts import UsersPostsView

urlpatterns = [
    path('users-posts/', UsersPostsView.as_view(), name='yozing-list'),
    path('detail/<int:pk>/', YozingDetailView.as_view(), name='yozing-list'),
    path('list/', YozingListView.as_view(), name='yozing-list'),
    path('update/<int:pk>/', YozingUpdateView.as_view(), name='yozing-update'),
    path('delete/<int:pk>/', YozingDeleteView.as_view(), name='yozing-delete'),
    path('create/', YozingCreateView.as_view(), name='yozing-create'),
]
