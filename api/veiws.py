from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

# This view handles both:
# GET  → return list of all students
# POST → create a new student
class StudentListCreate(generics.ListCreateAPIView):
    queryset         = Student.objects.all()
    serializer_class = StudentSerializer