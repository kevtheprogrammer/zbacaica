from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from account.views import *


urlpatterns = [
    path('', HomeView.as_view(),name="home"),
    path('about/', AboutView.as_view(),name="about"),
    path('contact/', ContactView.as_view(),name="contact"),
    path('menu/', include('account.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
