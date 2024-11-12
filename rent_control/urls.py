"""
URL configuration for rent_control project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import apps.core.views 


urlpatterns = [
    path('', apps.core.views.list_location, name='list-location'),
    path('form-client/', apps.core.views.form_client, name='client-create'),
    path('form-immobile/', apps.core.views.form_immobile, name='immobile-create'),
    path('form-location/<int:id>/', apps.core.views.form_location, name='location-create'), 
    path('reports/', apps.core.views.reports, name='reports'), 
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
