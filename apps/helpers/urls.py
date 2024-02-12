from django.urls import path

from helpers.views.about import AboutView
from helpers.views.categories import CategoriesListView
from helpers.views.contacts import ContactsView
from helpers.views.rules import RulesView
from helpers.views.tags import TagsListView

urlpatterns = [
    path('about/', AboutView.as_view()),
    path('contact/', ContactsView.as_view()),
    path('categoies', CategoriesListView.as_view()),
    path('rules/', RulesView.as_view()),
    path('tags', TagsListView.as_view())
]