from django.db import models
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    user = models.ForeignKey("users.User", related_name="events", verbose_name=_("user"))
    show = models.ForeignKey("shows.Show", related_name="events", verbose_name=_("show"))

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")
        ordering = ["user", "show", "id"]

    def __str__(self):
        return "{} - {}".format(self.user, self.show)
