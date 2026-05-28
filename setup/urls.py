
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # importa a url
    path('', include('apibox_app.urls')),
]
