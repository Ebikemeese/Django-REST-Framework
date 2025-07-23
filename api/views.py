from django.shortcuts import get_object_or_404
from students.models import Student
from .serializers import StudentSerializer, EmployeeSerializer, EmployerSerializer, EmploymentSerializer, EmploymentListSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from employers.models import Employer
from employments.models import Employment
from employment_list.models import EmploymentList
from django.http import Http404
from rest_framework import mixins, generics, viewsets
from blogs.models import Blog, Comment
from blogs.serializers import BlogSerializer, CommentSerializer
from .paginations import CustomPagination
from employment_list.filters import EmploymentListFilter
from rest_framework import filters as drf_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



# Create your views here.

#############   Function based view   #############

@api_view(['GET', 'POST'])
def students_view(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET', 'PUT', 'DELETE'])
def student_view(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
    
#############   Class based view   #############

class Employers(APIView):
    def get(self, request):
        employees = Employer.objects.all()
        serializer = EmployerSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EmployerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmployerDetail(APIView):
    def get_object(self, pk):
        try:
            return Employer.objects.get(pk=pk)
        except Employer.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployerSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployerSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#############   Mixings based view   #############

class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    

class EmployeeDetail(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
    
#############   Generics based view   #############

class Employments(generics.ListCreateAPIView):
    queryset = Employment.objects.all()
    serializer_class = EmploymentSerializer

class EmploymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employment.objects.all()
    serializer_class = EmploymentSerializer
    lookup_field = 'pk'

#############   Viewset based view   #############

class EmploymentListViewset(viewsets.ModelViewSet):
    queryset = EmploymentList.objects.all()
    serializer_class = EmploymentListSerializer
    pagination_class = CustomPagination
    filterset_class = EmploymentListFilter
    filter_backends = [drf_filters.SearchFilter, DjangoFilterBackend]

#############   Nested Serializer based view   #############

class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['id']
    search_fields = ['blog_title', 'blog_body']

class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
    
