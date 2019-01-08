from django.urls import path, include
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
    path('', views.index)
)

urlpatterns += (
    # urls for student
    path('fbla_admin/student/', views.studentListView.as_view(), name='fbla_admin_student_list'),
    path('fbla_admin/student/create/', views.studentCreateView.as_view(), name='fbla_admin_student_create'),
    path('fbla_admin/student/detail/<slug:slug>/', views.studentDetailView.as_view(), name='fbla_admin_student_detail'),
    path('fbla_admin/student/update/<slug:slug>/', views.studentUpdateView.as_view(), name='fbla_admin_student_update'),
)

urlpatterns += (
    # urls for book
    path('fbla_admin/book/', views.bookListView.as_view(), name='fbla_admin_book_list'),
    path('fbla_admin/book/create/', views.bookCreateView.as_view(), name='fbla_admin_book_create'),
    path('fbla_admin/book/detail/<slug:slug>/', views.bookDetailView.as_view(), name='fbla_admin_book_detail'),
    path('fbla_admin/book/update/<slug:slug>/', views.bookUpdateView.as_view(), name='fbla_admin_book_update'),
)

urlpatterns += (
    # urls for ebook
    path('fbla_admin/ebook/', views.ebookListView.as_view(), name='fbla_admin_ebook_list'),
    path('fbla_admin/ebook/create/', views.ebookCreateView.as_view(), name='fbla_admin_ebook_create'),
    path('fbla_admin/ebook/detail/<slug:slug>/', views.ebookDetailView.as_view(), name='fbla_admin_ebook_detail'),
    path('fbla_admin/ebook/update/<slug:slug>/', views.ebookUpdateView.as_view(), name='fbla_admin_ebook_update'),
    path('fbla_admin/ebook/delete/<slug:slug>/', views.ebookDeleteView.as_view(), name='fbla_admin_ebook_delete'),
)

