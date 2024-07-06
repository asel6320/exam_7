from django.urls import path

from webapp.views import index, create_note, update_note, delete_note

urlpatterns = [
    path('', index, name='main'),
    path('notes/create/', create_note, name='create_note'),
    path('note/<int:pk>/update/', update_note, name='update_note'),
    path('note/<int:pk>/delete/', delete_note, name='delete_note')
]