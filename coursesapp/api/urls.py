from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "coursesapp"

router = routers.DefaultRouter()
router.register("coursesapp", views.CourseViewSet)

urlpatterns = [
    path("subjects/", views.SubjetListView.as_view(), name="subject_list"),
    path("subjects/<pk>/", views.SubjectDetailView.as_view(), name="subject_detail"),
    # path('courses/<pk>/enroll/', views.CourseEnrollView.as_view(), name='course_enroll'),
    path("", include(router.urls)),
]
