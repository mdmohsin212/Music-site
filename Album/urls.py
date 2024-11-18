from django.urls import path, include
from Album.views import *

urlpatterns = [
    path('album/', album, name='album'),
    path('edit/<int:id>', edit, name='edit_album'),
    # path('delete/<int:id>', delete, name='delete_album'),
]
