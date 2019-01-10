from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from .models import student, book, ebook
from .forms import studentForm, bookForm, ebookForm
from django.shortcuts import redirect, render

class studentListView(ListView):
    model = student


class studentCreateView(CreateView):
    model = student
    form_class = studentForm


class studentDetailView(DetailView):
    model = student
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(studentDetailView, self).get_context_data(**kwargs)
        bookCount = ebook.objects.filter(check_out_student=self.object).count()
        booksCheckedOut = ebook.objects.filter(check_out_student=self.object)
        print(booksCheckedOut)
        toRetBooks = []
        for book in booksCheckedOut:
            toRetBooks.append(book.book_id)
        # Create any data and add it to the context
        context['bookCount'] = bookCount
        context['booksCheckedOut'] = toRetBooks
        return context


class studentUpdateView(UpdateView):
    model = student
    form_class = studentForm


class bookListView(ListView):
    model = book


class bookCreateView(CreateView):
    model = book
    form_class = bookForm


class bookDetailView(DetailView):
    model = book
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(bookDetailView, self).get_context_data(**kwargs)
        copyCount = ebook.objects.filter(book_id=self.object).count()
        booksCheckedOutCount = ebook.objects.filter(book_id=self.object).exclude(check_out_student=None).count()
        copies = ebook.objects.filter(book_id=self.object)
        toRetBooks = []
        # Create any data and add it to the context
        context['copyCount'] = copyCount
        context['booksCheckedOutCount'] = booksCheckedOutCount
        context['copies'] = copies
        context['students'] = student.objects.all()
        return context


class bookUpdateView(UpdateView):
    model = book
    form_class = bookForm


class ebookListView(ListView):
    model = ebook


class ebookCreateView(CreateView):
    model = ebook
    form_class = ebookForm
    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        return redirect(self.request.GET.get('next'))


class ebookDetailView(DetailView):
    model = ebook

class ebookDeleteView(DeleteView):
    model = ebook
    def get_success_url(self):
        return self.request.GET.get('next')

class ebookUpdateView(UpdateView):
    model = ebook
    form_class = ebookForm
    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        return redirect(self.request.GET.get('next'))

def index(request):
    context = {
        'bookCount': book.objects.count(),
        'studentCount': student.objects.count()
    }
    return render(request, 'fbla_admin/home.html', context=context)

def help(request):
    context = {
        'bookCount': book.objects.count(),
        'studentCount': student.objects.count()
    }
    return render(request, 'fbla_admin/help.html', context=context)
def documentation(request):
    context = {
        'bookCount': book.objects.count(),
        'studentCount': student.objects.count()
    }
    return render(request, 'fbla_admin/documentation.html', context=context)

def report(request):
    context = {}
    toRet = []
    for bok in book.objects.all():
        bok.count  = ebook.objects.filter(book_id=bok.id).count()
        bok.available = ebook.objects.filter(book_id=bok.id).exclude(check_out_student=None).count()
        toRet.append(bok)
    context['students'] = []
    for studen in student.objects.all():
        studen.count = ebook.objects.filter(check_out_student=studen.id).count()
        context['students'].append(studen)
    context['books'] = toRet
    print(context)
    return render(request, 'fbla_admin/report.html', context=context)