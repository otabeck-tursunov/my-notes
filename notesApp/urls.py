from django.urls import path
from .views import *

urlpatterns = [
    path('notes/', NoteList.as_view(), name='note-list'),
    path('notes/<int:pk>/', NoteDetail.as_view(), name='note-detail')
]