from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #Django Admin
    path('anything-but-admin/', admin.site.urls),

    #User managment
    path('accounts/', include('allauth.urls')),

    #Local apps
    path('',include('pages.urls')),
    path('books2/', include('books2.urls')),
    path('orders/', include('orders.urls')),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns