from django import forms
from .models import student, book, ebook


class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'grade_level']


class bookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = ['name', 'author', 'genre', 'image']


class ebookForm(forms.ModelForm):
    class Meta:
        model = ebook
        fields = ['name', 'check_out_student', 'book_id']


