from rest_framework import viewsets, generics
from school.models import Student, Course, Registration
from school.serializers import StudentSerializer, CourseSerializer, \
                               RegistrationSerializer, RegistrationStudentListSerializer, \
                               RegistrationCourseListSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentsViewSet(viewsets.ModelViewSet):
    """ Show all students """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CoursesViewSet(viewsets.ModelViewSet):
    """ Show all courses """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class RegistrationsViewSet(viewsets.ModelViewSet):
    """ Show all registrations """
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class RegistrationStudentListViewSet(generics.ListAPIView):
    """ List student registrations """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Registration.objects.filter(student_id=self.kwargs.get('pk'))

    serializer_class = RegistrationStudentListSerializer


class RegistrationCourseListViewSet(generics.ListAPIView):
    """ List student registrations """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Registration.objects.filter(course_id=self.kwargs.get('pk'))

    serializer_class = RegistrationCourseListSerializer
