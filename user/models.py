import random
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import Group, Permission
from django.utils import timezone
import datetime
TIME = 5  # Misol uchun 5 daqiqa

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Berilgan elektron pochta va parol bilan foydalanuvchini yaratib saqlaydi.
        """
        if not email:
            raise ValueError("Berilgan elektron pochta kiritilmagan")

        email = self.normalize_email(email)  # Emailni normalizatsiya qilish
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superfoydalanuvchi is_staff=True bo'lishi kerak.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superfoydalanuvchi is_superuser=True bo'lishi kerak.")
        return self._create_user(email, password, **extra_fields)

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)



class UserConfirmation(models.Model):
    user = models.OneToOneField(
        'User',
        on_delete=models.CASCADE,
        related_name='confirmation',
    )
    code = models.CharField(max_length=4)
    expire_datetime = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.expire_datetime:
            self.expire_datetime = timezone.now() + datetime.timedelta(minutes=TIME)
        super(UserConfirmation, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.code} {self.user.email}"


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = None
    class GenderType(models.TextChoices):
        MAN = "Erkak", "Erkak"
        WOMAN = "Ayol", "Ayol"
    
    class Type(models.TextChoices):
        HARIDOR = "Haridor", "Haridor"
        SOTUVCHI = "Sotuvchi", "Sotuvchi"
        ADMIN = "Admin", "Admin"
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name='guruhlar',
        blank=True,
        related_name='%(class)s_related_groups', # related_name o'zgarish
        related_query_name='%(class)s_related_group',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='foydalanuvchi ruxsatlar',
        blank=True,
        related_name='%(class)s_related_user_permissions', # related_name o'zgarish
        related_query_name='%(class)s_related_user_permission',
    )
    type = models.CharField(Type, max_length=10)
    gender = models.CharField(GenderType, max_length=5)
    auth_status = models.BooleanField(default=False)
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    
    def get_code(self):
        confirmation = UserConfirmation.objects.filter(user=self).first()
        code = ''.join([str(random.randint(0, 1000))[-1] for _ in range(4)])
        if confirmation:
            confirmation.code = code
            confirmation.save(update_fields=['code'])
        else:
            UserConfirmation.objects.create(user=self, code=code)
        return code