from django.db import models
from django.utils.translation import ugettext_lazy as _


class Show(models.Model):
    datetime = models.DateTimeField(verbose_name=_("datetime"))
    cinema = models.ForeignKey("cinemas.Cinema", related_name="shows", verbose_name=_("cinema"))
    movie = models.ForeignKey("movies.Movie", related_name="shows", verbose_name=_("movie"))

    class Meta:
        verbose_name = _("show")
        verbose_name_plural = _("shows")
        ordering = ["datetime", "cinema", "id"]

    def __str__(self):
        return "{} - {} - {}".format(self.datetime.strftime("%d/%m/%y %H:%M"),
                                     self.movie,
                                     self.cinema)
