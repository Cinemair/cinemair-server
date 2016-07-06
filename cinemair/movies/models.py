from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_pgjson.fields import JsonBField

from cinemair.common.thirdparty import themoviedb as tmdb


class Movie(models.Model):
    name = models.CharField(max_length=500, verbose_name=_("name"))
    tmdb_id = models.IntegerField(null=True, blank=True, verbose_name=_("themoviedb id"))
    tmdb_info = JsonBField(null=True, blank=True, verbose_name=_("themoviedb info"))
    tmdb_videos= JsonBField(null=True, blank=True, verbose_name=_("themoviedb videos"))

    class Meta:
        verbose_name = _("movie")
        verbose_name_plural = _("movies")

    def __str__(self):
        return self.name

    def _set_movi_info_from_tmdb(self):
        if self.tmdb_id:
            self.tmdb_info = tmdb.movie_info(self.tmdb_id)
            self.tmdb_videos = tmdb.movie_videos(self.tmdb_id)

        if self.tmdb_info and "title" in self.tmdb_info:
            self.name = self.tmdb_info["title"]

    def save(self, *args, **kwargs):
        self._set_movi_info_from_tmdb()
        return super().save(*args, **kwargs)
