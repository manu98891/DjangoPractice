from django.urls import path
from . import views


urlpatterns = [
    # path('',hello) Llamar a la funcion que se encuentra en myapp
    path('',views.hello),
    path('about/',views.about)
]
