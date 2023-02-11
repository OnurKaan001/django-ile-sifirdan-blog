from django.urls import path, include
from .views import index_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index_view, name="index"),
    path("ckeditor", include("ckeditor_uploader.urls"), name="ckeditor"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)