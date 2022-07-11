from django.urls import path
from django.contrib import admin
from students import views

urlpatterns = [
    path('', views.index,  name="index"),
    path('students/', views.getAll,  name="students.getAll"),
    path('students/<int:pk>', views.detail, name="students.detail"),
    path('students/<int:pk>/edit', views.UpdateStudentView.as_view(), name="students.update"),
    path('students/delete/<int:pk>', views.remove, name="students.delete"),
    path('students/search', views.search, name="students.search"),
    path('students/add', views.CreateStudentView.as_view(), name="students.add"),
]