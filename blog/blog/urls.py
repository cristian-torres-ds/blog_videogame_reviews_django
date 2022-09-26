from django.urls import path, include
from blog.views import *
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='app_super/logout.html'), name='logout'),
    path('editar_perfil', editar_perfil, name='editar_perfil'),
    path('add_avatar/', add_avatar, name='add_avatar'),
    # apps
    path('posteos/', include('posteos.urls')),
    path('mensajes/', include('mensajes.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)