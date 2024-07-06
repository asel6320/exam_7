from django.urls import path

from webapp.views import index, create_note

urlpatterns = [
    path('', index, name='main'),
    path('create/', create_note, name='create_note'),
    #path('task/', task_detail),
]