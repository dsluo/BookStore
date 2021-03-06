from django.urls import re_path
from django.contrib.auth import settings
from django.conf.urls.static import static


from books import views as books_views

app_name = "books"

urlpatterns = [
    re_path(r'^$', books_views.landing, name='landing'),
    re_path(r'^home/$', books_views.home, name='home'),

    re_path(r'^book/$', books_views.all_books, name="query"),
    re_path(r'^book/(?P<slug>[\w-]+)/$', books_views.detail, name='detail'),
    # make / url pattern redirect to home/ if logged in
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)