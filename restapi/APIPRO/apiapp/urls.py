
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.BlogpostListCreate.as_view()),
    path("<int:pk>/",views.BlogpostRetriveUpdate.as_view())
]