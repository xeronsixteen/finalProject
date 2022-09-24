from django.urls import path

from webapp.views.album import UpdateAlbum, DeleteAlbum, OneAlbumView, CreateAlbum
from webapp.views.photos import IndexView, CreatePhoto, UpdatePhoto, PhotoView, DeletePhoto, FavView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('photo/add/', CreatePhoto.as_view(), name="add"),
    path('photo/<int:pk>/update/', UpdatePhoto.as_view(), name="update"),
    path('photo/<int:pk>/', PhotoView.as_view(), name="photo_view"),
    path('photo/<int:pk>/delete/', DeletePhoto.as_view(), name="delete"),
    path('album/<int:pk>/update/', UpdateAlbum.as_view(), name="update_album"),
    path('album/<int:pk>/delete/', DeleteAlbum.as_view(), name="delete_album"),
    path('album/add/', CreateAlbum.as_view(), name="add_album"),
    path('album/<int:pk>/', OneAlbumView.as_view(), name="one_album"),
    path('fav/<int:pk>/', FavView.as_view(), name='fav'),

]
