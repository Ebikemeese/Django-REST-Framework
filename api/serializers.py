from rest_framework import serializers
from students.models import Student
from employees.models import Employee
from employers.models import Employer
from employments.models import Employment
from employment_list.models import EmploymentList


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = "__all__"

class EmploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employment
        fields = "__all__"

class EmploymentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentList
        fields = "__all__"