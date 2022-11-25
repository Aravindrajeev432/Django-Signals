
from django.urls import path
from . import views
urlpatterns =[
    path("",views.ShowStore.as_view(),name="store"),
]