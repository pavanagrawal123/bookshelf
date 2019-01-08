from django.contrib import admin
from django import forms
from .models import student, book, ebook

class studentAdminForm(forms.ModelForm):

    class Meta:
        model = student
        fields = '__all__'


class studentAdmin(admin.ModelAdmin):
    form = studentAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'grade_level']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'grade_level']

admin.site.register(student, studentAdmin)


class bookAdminForm(forms.ModelForm):

    class Meta:
        model = book
        fields = '__all__'


class bookAdmin(admin.ModelAdmin):
    form = bookAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'author', 'genre']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'author', 'genre']

admin.site.register(book, bookAdmin)


class ebookAdminForm(forms.ModelForm):

    class Meta:
        model = ebook
        fields = '__all__'


class ebookAdmin(admin.ModelAdmin):
    form = ebookAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(ebook, ebookAdmin)


