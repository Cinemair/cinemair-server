from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import UserManager, AbstractBaseUser
from django.core import validators
from django.utils import timezone

import re


class PermissionsMixin(models.Model):
    """
    A mixin class that adds the fields and methods necessary to support
    Django"s Permission model using the ModelBackend.
    """
    is_superuser = models.BooleanField(_("superuser status"), default=False,
        help_text=_("Designates that this user has all permissions without "
                    "explicitly assigning them."))

    class Meta:
        abstract = True

    @property
    def is_staff(self):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_active and self.is_superuser

    def has_perms(self, perm_list, obj=None):
        return self.is_active and self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_active and self.is_superuser


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(null=False, blank=False, unique=True, max_length=255, verbose_name=_("username"),
                                help_text=_("Required. 255 characters or fewer. Letters, numbers and "
                                            "/./-/_ characters"),
                                validators=[validators.RegexValidator(re.compile("^[\w.-]+$"),
                                                                      _("Enter a valid username."),
                                                                      "invalid")])
    email = models.EmailField(null=False, blank=False, unique=True, max_length=255,
                              verbose_name=_("email address"))
    full_name = models.CharField(null=False, blank=True, max_length=256, verbose_name=_("full name"))

    is_active = models.BooleanField(default=True, verbose_name=_("active"),
                                    help_text=_("Designates whether this user should be treated as "
                                                "active. Unselect this instead of deleting accounts."))
    date_joined = models.DateTimeField(null=False, blank=False, default=timezone.now,
                                       verbose_name=_("date joined"))


    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "full_name"]

    objects = UserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["username"]

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.full_name or self.username or self.email
