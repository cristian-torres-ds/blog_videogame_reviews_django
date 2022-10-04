from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import inicio


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    # apps
    path('posteos/', include('posteos.urls')),
    path('mensajes/', include('mensajes.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)