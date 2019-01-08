from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import SmallIntegerField
from django.db.models import TextField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class student(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    grade_level = models.SmallIntegerField()


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('fbla_admin_student_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('fbla_admin_student_update', args=(self.slug,))


class book(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    image = models.ImageField(verbose_name="Cover Image", upload_to="book_images/", blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('fbla_admin_book_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('fbla_admin_book_update', args=(self.slug,))


class ebook(models.Model):

    # Fields
    name = models.CharField(max_length=255, verbose_name="Claim Code", unique=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    check_out_student = models.ForeignKey(
        'fbla_admin.student',
        on_delete=models.CASCADE, related_name="students",
        blank=True,
        null=True
    )
    book_id = models.ForeignKey(
        'fbla_admin.book',
        on_delete=models.CASCADE, related_name="books",
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('fbla_admin_ebook_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('fbla_admin_ebook_update', args=(self.slug,))


