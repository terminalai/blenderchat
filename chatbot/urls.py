from django.urls import path
from .views import ListMessage, DetailMessage

urlpatterns = [
    path('', ListMessage.as_view()),
    path('<int:pk>', DetailMessage.as_view()),
]
