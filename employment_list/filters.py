from django_filters import rest_framework as filters
from .models import EmploymentList


class EmploymentListFilter(filters.FilterSet):
    emp_name = filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    id = filters.CharFilter(field_name='id')
    class Meta:
        model = EmploymentList
        fields = ['emp_name', 'id']