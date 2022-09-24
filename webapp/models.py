from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.

class Photo(models.Model):
    image = models.ImageField(upload_to='images', blank=False, null=False, verbose_name='image')
    description = models.TextField(null=False, blank=False, verbose_name='description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="date of creation")
    user = models.ManyToManyField(get_user_model(), verbose_name='User', related_name='photos')
    album = models.ForeignKey('webapp.Album', on_delete=models.CASCADE, blank=True, related_name='photos',
                              verbose_name='photos')
    public = models.BooleanField(default=True)
    fav = models.ManyToManyField(get_user_model(), related_name='fav', blank=True)

    def __str__(self):
        return f"{self.id}. {self.description}: {self.user}"

    def get_absolute_url(self):
        return reverse("webapp:photo_view", kwargs={"pk": self.pk})

    def total_favs(self):
        return self.fav.count()

    class Meta:
        db_table = "photos"
        verbose_name = "photos"
        verbose_name_plural = "Photos"


class Album(models.Model):
    created_at = models.DateField(blank=True, verbose_name="date of creation")
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='album name')
    description = models.TextField(null=True, blank=True, verbose_name='album description')
    user = models.ManyToManyField(get_user_model(), verbose_name='User', related_name='albums')
    public = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.name}"

    # class Meta:
    #     db_table = "albums"
    #     verbose_name = "albums"
    #     verbose_name_plural = "albums"
