from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpRequest, HttpResponse
from django.http import Http404
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm


class CreateStudentView(CreateView):
    model = Student
    success_url ="/students/"
    form_class = StudentForm
    
class UpdateStudentView(UpdateView):
    model = Student
    success_url ="/students/"
    form_class = StudentForm
def remove(request, pk):
    student = get_object_or_404(Student, id = pk)
    if request.method =="POST":
        student.delete()
        return HttpResponseRedirect("/")
    return render(request, "students/student_delete.html", {})

def search(request: HttpRequest):
    if request.method =="POST":
        keyword = request.POST.get('keyword')
        students = Student.objects.filter(name__icontains=keyword)
        if len(students)>0:
            return render(request, "students/students_list.html", {"students": students})
        else:
            return render(request, "notfound.html", {})
    return render(request, "notfound.html", {})

def index(request):
    students = Student.objects.all()
    return render(request, "students/index.html", {"students": students})


def getAll(request):
    students = Student.objects.all()
    return render(request, "students/students_list.html", {"students": students})

def detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except  Student.DoesNotExist:
        raise Http404("Student not found")
    return render(request, "students/student_detail.html", {"student": student})