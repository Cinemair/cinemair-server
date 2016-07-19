from django.db import models
from django.utils.translation import ugettext_lazy as _


class Favorite(models.Model):
    user = models.ForeignKey("users.User", related_name="favorites", verbose_name=_("user"))
    show = models.ForeignKey("shows.Show", related_name="favorites", verbose_name=_("show"))

    class Meta:
        verbose_name = _("favorite")
        verbose_name_plural = _("favorites")
        ordering = ["user", "show", "id"]

    def __str__(self):
        return "{} - {}".format(self.user, self.show)
