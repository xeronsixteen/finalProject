from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import AlbumForm
from webapp.models import Album


# class AllAlbumsView(ListView):
#     template_name = 'albums/albums.html'
#     context_object_name = 'albums'
#
#     def get_queryset(self):
#         return Album.objects.all().order_by('-created_at')


class OneAlbumView(LoginRequiredMixin, DetailView):
    template_name = "albums/one_album.html"
    model = Album

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = self.object.photos.order_by("-created_at")
        return context


class CreateAlbum(LoginRequiredMixin, CreateView):
    form_class = AlbumForm
    template_name = "albums/new.html"

    def get_success_url(self):
        return reverse('webapp:one_album', kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        project = form.save()
        user_id = self.request.user
        project.user.add(user_id)
        project.save()
        return super().form_valid(form)


class UpdateAlbum(PermissionRequiredMixin, UpdateView):
    model = Album
    template_name = 'albums/update.html'
    form_class = AlbumForm
    context_object_name = 'album'
    permission_required = 'webapp.change_album'

    def get_success_url(self):
        return reverse('webapp:album_list')


class DeleteAlbum(PermissionRequiredMixin, DeleteView):
    model = Album
    context_object_name = 'album'
    template_name = 'albums/delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_album'
