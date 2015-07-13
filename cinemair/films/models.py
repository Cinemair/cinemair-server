from django.db import models
from django.utils.translation import ugettext_lazy as _


class Film(models.Model):
    name = models.CharField(max_length=500, verbose_name=_("name"))
    mdb_id = models.IntegerField(null=True, blank=True, verbose_name=_("themoviedb id"))

    class Meta:
        verbose_name = _("film")
        verbose_name_plural = _("films")

    def __str__(self):
        return self.name
