from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .settings import DEBUG

urlpatterns = [
    path("admin/", admin.site.urls),

    # Login / Logout
    path('account/', include('django.contrib.auth.urls')),

    # my apps
    path('todo/', include('todo.urls')),
    path('', include('main.urls')),
    path('profiles/', include('profiles.urls'))

]

if DEBUG is True:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configure Admin Title
admin.site.site_header = "School Administration"
admin.site.site_title = "School"
admin.site.index_title = "Welcome to School"
