from django.contrib import admin
from django.contrib.auth.models import Group as DjangoGroup
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.utils.translation import ugettext_lazy as _

from .models import User
from .forms import UserCreationForm
from .forms import UserChangeForm


admin.site.unregister(DjangoGroup)


@admin.register(User)
class Users(DjangoUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("full_name", "email")}),
        (_("Permissions"), {"fields": ("is_active", "is_superuser")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2"),
        }),
    )
    list_display = ("username", "email", "full_name", "is_superuser")
    list_filter = ("is_active", "is_superuser",)
    search_fields = ("email","username", "full_name")
    ordering = ("email",)
    filter_horizontal = ()
