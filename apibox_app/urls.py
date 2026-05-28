from django.urls import path
from apibox_app.views import box  # se for usar suas views aqui

urlpatterns = [
    path('box/', box, name='box'),
    # Suas rotas entram aqui, por exemplo:
    # path('', views.home, name='home'),
]