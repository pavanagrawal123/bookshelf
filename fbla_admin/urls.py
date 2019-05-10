from django.urls import path, include
from django.contrib.auth.decorators import login_required, permission_required

from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'student', api.studentViewSet)
router.register(r'book', api.bookViewSet)
router.register(r'ebook', api.ebookViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
    path('', views.index),
    path('help/', views.help),
    path('progDoc/', views.documentation),
    path('report/', views.report)
)

urlpatterns += (
    # urls for student
    path('fbla_admin/student/', login_required(views.studentListView.as_view()), name='fbla_admin_student_list'),
    path('fbla_admin/student/create/', login_required(views.studentCreateView.as_view()), name='fbla_admin_student_create'),
    path('fbla_admin/student/detail/<slug:slug>/', login_required(views.studentDetailView.as_view()), name='fbla_admin_student_detail'),
    path('fbla_admin/student/update/<slug:slug>/', login_required(views.studentUpdateView.as_view()), name='fbla_admin_student_update'),
)

urlpatterns += (
    # urls for book
    path('fbla_admin/book/', login_required(views.bookListView.as_view()), name='fbla_admin_book_list'),
    path('fbla_admin/book/create/', login_required(views.bookCreateView.as_view()), name='fbla_admin_book_create'),
    path('fbla_admin/book/detail/<slug:slug>/', login_required(views.bookDetailView.as_view()), name='fbla_admin_book_detail'),
    path('fbla_admin/book/update/<slug:slug>/', login_required(views.bookUpdateView.as_view()), name='fbla_admin_book_update'),
)

urlpatterns += (
    # urls for ebook
    path('fbla_admin/ebook/', login_required(views.ebookListView.as_view()), name='fbla_admin_ebook_list'),
    path('fbla_admin/ebook/create/', login_required(views.ebookCreateView.as_view()), name='fbla_admin_ebook_create'),
    path('fbla_admin/ebook/detail/<slug:slug>/', login_required(views.ebookDetailView.as_view()), name='fbla_admin_ebook_detail'),
    path('fbla_admin/ebook/update/<slug:slug>/', login_required(views.ebookUpdateView.as_view()), name='fbla_admin_ebook_update'),
    path('fbla_admin/ebook/delete/<slug:slug>/', login_required(views.ebookDeleteView.as_view()), name='fbla_admin_ebook_delete'),
)

