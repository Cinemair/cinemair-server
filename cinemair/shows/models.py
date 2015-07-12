from django.db import models
from django.utils.translation import ugettext_lazy as _


class Show(models.Model):
    datetime = models.DateTimeField(verbose_name=_("datetime"))
    cinema = models.ForeignKey("cinemas.Cinema", related_name="shows", verbose_name=_("cinema"))
    film = models.ForeignKey("films.Film", related_name="shows", verbose_name=_("film"))

    class Meta:
        verbose_name = _("show")
        verbose_name_plural = _("shows")
