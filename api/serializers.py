from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Student      # which model to use
        fields = '__all__'    # include all columns