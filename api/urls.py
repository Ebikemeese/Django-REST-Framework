from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employment_lists', views.EmploymentListViewset, basename='employment_list')

urlpatterns = [
    path('students/', views.students_view),
    path('students/<int:pk>/', views.student_view),
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
    path('employers/', views.Employers.as_view()),
    path('employers/<int:pk>/', views.EmployerDetail.as_view()),
    path('employments/', views.Employments.as_view()),
    path('employments/<int:pk>/', views.EmploymentDetail.as_view()),
    path('', include(router.urls)),
    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentView.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),

]