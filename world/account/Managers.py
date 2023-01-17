from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, **extra_fields):
        if not email:
            raise ValueError("please provide email")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        # user.set_password(password)
        user.set_unusable_password()
        user.save()
        return user

    def create_superuser(self, email):
        user = self.create_user(email)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user