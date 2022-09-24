from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo


# Create your views here.

class FavView(LoginRequiredMixin, View):
    def get(self, request, *args, pk, **kwargs):
        photo = Photo.objects.get(pk=pk)
        user = self.request.user
        if user in photo.fav.all():
            photo.fav.remove(user)
        else:
            photo.fav.add(user)
        return JsonResponse ({'count': photo.fav.count()})




class IndexView(ListView):  # пермишны на забудь
    template_name = 'photos/index.html'
    context_object_name = 'photos'

    def get_queryset(self):
        return Photo.objects.all().order_by('created_at')


class PhotoView(LoginRequiredMixin, DetailView):  # пермишны на забудь
    template_name = "photos/photo.html"
    model = Photo
    context_object_name = 'photo_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreatePhoto(LoginRequiredMixin, CreateView):  # пермишны на забудь
    form_class = PhotoForm
    template_name = "photos/create.html"

    def get_success_url(self):
        return reverse('webapp:index')


class UpdatePhoto(PermissionRequiredMixin, UpdateView):  # пермишны на забудь
    model = Photo
    template_name = 'photos/update.html'
    form_class = PhotoForm
    context_object_name = 'photo'
    permission_required = 'webapp.change_photo'

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})


class DeletePhoto(PermissionRequiredMixin, DeleteView):  # пермишны на забудь
    model = Photo
    context_object_name = 'photo'
    template_name = 'photos/delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_photo'
