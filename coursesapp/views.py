from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from coursesapp import models as coursesapp_models


class OwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.requesrt.user)


class OwnerEditMixin:
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin, PermissionRequiredMixin):
    model = coursesapp_models.Course
    fields = ("subject", "title", "overview")
    success_url = reverse_lazy("manage_course_list")


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name = "coursesapp/manage/course/form.html"


class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = "coursesapp/manage/course/list.html"
    permission_required = "coursesapp.view_course"


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    permission_required = "coursesapp.add_course"


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    permission_required = "coursesapp.change_course"


class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = "coursesapp/manage/course/delete.html"
    permission_required = "coursesapp.delete_course"
