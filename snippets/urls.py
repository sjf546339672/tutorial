# coding: utf-8
from django.urls import path, include
from snippets import views
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    path('snippet_list/', views.snippet_list),
    path('snippet_list/<int:pk>/', views.snippet_detail),
    path('snippet_list_one/', views.snippet_list_one),
    path('snippet_list_one/<int:pk>/', views.snippet_list_one),
    path('snippets_one/', views.SnippetList.as_view()),
    path('snippets_one/<int:pk>/', views.SnippetDetail.as_view()),
    path('snippets_two/', views.SnippetMixinsList.as_view()),
    path('snippets_two/<int:pk>/', views.SnippetDetail.as_view()),
    path('snippets_three/', views.SnippetGenericList.as_view()),
    path('snippets_three/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('schema/', schema_view),
]
