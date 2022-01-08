from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from school.views import StudentsViewSet, CoursesViewSet, \
                         RegistrationsViewSet, RegistrationStudentListViewSet, \
                         RegistrationCourseListViewSet


router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Students')
router.register('courses', CoursesViewSet, basename='Courses')
router.register('registrations', RegistrationsViewSet, basename='Registrations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('student/<int:pk>/registrations/', RegistrationStudentListViewSet.as_view()),
    path('course/<int:pk>/registrations/', RegistrationCourseListViewSet.as_view()),
]
