from django.urls import path
from . import views


urlpatterns = [
    path('', views.servicios, name="servicios"),
]


# urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)