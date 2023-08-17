from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from dry_rest_permissions.generics import authenticated_users


class User(AbstractUser):
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=250)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    app_id = models.CharField(
        _('app Id'),
        max_length=255,
        null=True,
        blank=True
    )
    dev_id = models.CharField(
        _('dev Id'),
        max_length=255,
        null=True,
        blank=True
    )
    cert_id = models.CharField(
        _('cert Id'),
        max_length=255,
        null=True,
        blank=True
    )
    ebay_token = models.CharField(
        _('ebay Token'),
        max_length=3000,
        null=True,
        blank=True
    )

    
    def has_read_permission(request):
        return True

    def has_register_permission(request):
        return True

    def has_login_permission(request):
        return True
    
    @authenticated_users
    def has_get_ebay_info_permission(request):
        return True

    @authenticated_users
    def has_write_permission(request):
        return True

    @authenticated_users
    def has_object_write_permission():
        return True
