from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView

from coursesapp import models as coursesapp_models
from studentsapp.forms import CourseEnrollForm


class StudentRegistrationView(CreateView):
    template_name = "studentsapp/student/registration.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("student_course_list")

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd["username"], password=cd["password1"])
        login(self.request, user)
        return result


class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data["course"]
        # print(self.course, type(self.course))
        print(3232323)
        self.course.students.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("student_course_detail", args=[self.course.id])


class StudentCourseListView(LoginRequiredMixin, ListView):
    model = coursesapp_models.Course
    template_name = "studentsapp/course/list.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])


class StudentCourseDetailView(DetailView):
    model = coursesapp_models.Course
    template_name = "studentsapp/course/detail.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        course = self.get_object()  # почему не self.object
        if "module_id" in self.kwargs:
            context["module"] = course.modules.get(id=self.kwargs["module_id"])
        else:
            context["module"] = course.modules.all()[0]

        return context
