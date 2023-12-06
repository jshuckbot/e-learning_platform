from django.urls import path

from chatapp import views

app_name = "chatapp"

urlpatterns = [
    path("room/<int:course_id>/", views.course_chat_room, name="course_chat_room"),
]
