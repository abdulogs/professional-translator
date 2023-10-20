from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from smartfields import fields


class UserManager(BaseUserManager):
    use_in_migraions = True

    def create_user(self, email, password, password2=None, **extra_fields):
        if not email:
            raise ValueError(("Email address is require"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(("Superuser must have is_staff true"))

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    username = models.CharField('username', max_length=150, unique=True)
    email = models.EmailField('email address', unique=True, max_length=255)
    avatar = fields.ImageField(
        upload_to="avatars", blank=True, null=True, default="avatar.png")
    is_active = models.BooleanField(null=True, blank=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


class BlogCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(null=True, blank=True, default=True)
    created_by = models.ForeignKey(
        User, editable=False, null=True,  blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blog_categories'
        verbose_name = 'Blog category'
        verbose_name_plural = 'Blog categories'


class Blog(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True, default="")
    category = models.ForeignKey(
        BlogCategory, null=True, blank=True, on_delete=models.SET_NULL)
    image = fields.ImageField(
        upload_to="blogs", null=True, blank=True, default="placeholder.png")
    alt = models.CharField(max_length=100, null=True, blank=True, default="")
    is_active = models.BooleanField(null=True, blank=True, default=True)
    created_by = models.ForeignKey(
        User, editable=False, null=True,  blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blogs'
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'


class Faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=5000)
    is_active = models.BooleanField(null=True, blank=True, default=True)
    created_by = models.ForeignKey(
        User, editable=False, null=True,  blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'faqs'
        verbose_name = 'Faq'
        verbose_name_plural = 'Faqs'


class Query(models.Model):
    fullname = models.CharField(max_length=200, null=True,  blank=True)
    email = models.CharField(max_length=200, null=True,  blank=True)
    phone = models.CharField(max_length=200, null=True,  blank=True)
    message = models.TextField(null=True,  blank=True)
    reply = models.TextField(null=True,  blank=True)
    document = fields.FileField(
        upload_to="queries", blank=True, null=True, default="")
    is_active = models.BooleanField(null=True, blank=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Subscriber(models.Model):
    email = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(null=True, blank=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Newsletter(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=5000, null=True, blank=True)
    is_active = models.BooleanField(null=True, blank=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'newsletters'
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'
