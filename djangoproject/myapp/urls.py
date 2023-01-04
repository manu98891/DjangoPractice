from django.urls import path
from . import views


urlpatterns = [
    # path('',hello) Llamar a la funcion que se encuentra en myapp
    path('',views.index),
    path('about/',views.about),
    path('hello/<str:user>',views.hello),
    path('projects/', views.projects),
    path('task/<int:id>', views.task)
]
