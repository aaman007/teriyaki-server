from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser as BaseUser, UserManager as BaseUserManager

from allauth.socialaccount.models import SocialAccount


class UserManager(BaseUserManager):
    pass


class User(BaseUser):
    phone_number = models.CharField(verbose_name=_('Phone Number'), max_length=15, blank=True)

    objects = UserManager()

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return f'{self.first_name}{self.last_name}'

    def get_social_data(self, provider: str = 'google'):
        try:
            account = SocialAccount.objects.filter(user=self, provider='google').first()
            return (account and account.extra_data) or dict()
        except SocialAccount.DoesNotExist:
            return dict()


class Address(models.Model):
    user = models.ForeignKey(
        verbose_name=_('User'),
        to='User',
        related_name='addresses',
        on_delete=models.CASCADE
    )
    street = models.CharField(verbose_name=_('Street'), max_length=150)
    city = models.CharField(verbose_name=_('City'), max_length=150)
    postal_code = models.PositiveIntegerField(verbose_name=_('Postal Code'))

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    def __str__(self):
        return self.city
