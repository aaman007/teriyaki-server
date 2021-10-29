from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import AbstractUser as BaseUser, UserManager as BaseUserManager


class UserManager(BaseUserManager):
    pass


class User(BaseUser):
    objects = UserManager()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_social_data(self, provider: str = 'google'):
        try:
            account = SocialAccount.objects.filter(user=self, provider='google').first()
            return account.extra_data or dict()
        except SocialAccount.DoesNotExist:
            return dict()
