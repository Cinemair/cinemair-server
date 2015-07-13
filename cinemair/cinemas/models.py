from django.db import models
from django.utils.translation import ugettext_lazy as _


class Cinema(models.Model):
    name = models.CharField(max_length=500, verbose_name=_("name"))
    address = models.TextField(null=True, blank=True, verbose_name=_("address"))
    city = models.CharField(max_length=500, null=True, blank=True, verbose_name=_("city"))
    country = models.CharField(max_length=500, null=True, blank=True, verbose_name=_("country"))

    class Meta:
        verbose_name = _("cinema")
        verbose_name_plural = _("cinemas")

    def __str__(self):
        return self.name
