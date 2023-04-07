from django.shortcuts import render,redirect, get_object_or_404
from .models import Student, Course
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# from .models import Student_results
from .forms import StudentForm, CourseForm
from django.contrib.auth.decorators import login_required

@login_required
def admission(request):
    if request.method == 'GET':
        return render(request, 'app1/admission.html', {'form': StudentForm()})
    else:
        try:
            form = StudentForm(request.POST)
            if form.is_valid():
                student = form.save()
                course = Course.objects.create(student=student, course_name=request.POST['course_name'], course_sem=request.POST['course_sem'])
                course.save()
                return redirect('admission')
            else:
                return render(request, 'app1/admission.html', {'form': form, 'error': 'Bad data passed in'})
        except ValueError:
            return render(request, 'app1/admission.html', {'form': StudentForm(), 'error': 'Bad data passed in'})

def home(request):
    return render(request, 'app1/home.html')

@login_required
def student_table_approved(request):
    students = Student.objects.select_related('course').all()
    return render(request, 'app1/student_table_approved.html',{'students': students})

@login_required
def student_table_unapproved(request):
    students = Student.objects.select_related('course').all()
    return render(request, 'app1/student_table_unapproved.html',{'students': students})

@login_required
def edit_student_info(request, student_pk):
    students = get_object_or_404(Student,pk=student_pk)
    if request.method == 'GET':
        form = StudentForm(instance=students)
        return render(request, 'app1/edit_student_info.html', {'students': students, 'form':form})
    else:
        try:
            form = StudentForm(request.POST, instance=students)
            form.save()
            return redirect('student_table_unapproved')
        except ValueError:
            return render (request, 'app1/edit_student_info.html', {'form':StudentForm(), 'students': students,'error':'Bad data passed in'})

@login_required
def delete_student(request, student_pk):
    student = get_object_or_404(Student,pk=student_pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_table_approved')

@login_required
def student_results(request, student_pk):
    res = get_object_or_404(Course, pk=student_pk)
    return render(request, 'app1/student_results.html', {'res':res})

@login_required
def all_students_results(request):
    results = Course.objects.all()
    return render(request, 'app1/all_students_results.html', {'results':results})

@login_required
def create_result(request):
    if request.method == 'GET':
        return render (request, 'app1/create_result.html', {'form':CourseForm()})
    else:
        try:
            form = CourseForm(request.POST)
            newnote = form.save(commit=False)
            newnote.save()                
            return redirect('create_result')
        except ValueError:
            return render (request, 'app1/create_result.html', {'form':CourseForm(), 'error':'Bad data passed in'})  

@login_required
def edit_course_results(request, student_pk):
    students = get_object_or_404(Course,pk=student_pk)
    if request.method == 'GET':
        form = CourseForm(instance=students)
        return render(request, 'app1/edit_course_results.html', {'students': students, 'form':form})
    else:
        try:
            form = CourseForm(request.POST, instance=students)
            form.save()
            return redirect('all_students_results')
        except ValueError:
            return render (request, 'app1/edit_course_results.html', {'form':CourseForm(), 'students': students,'error':'Bad data passed in'})


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'app1/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            if (request.POST['password1'] == request.POST['password2']):
                try:
                    user = User.objects.create_user(request.POST['username'],password = request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('home')
                except IntegrityError:
                    return render (request, 'app1/signupuser.html', {'form':UserCreationForm(), 'error':'Username has already been taken, plz choose new username'})                
            else:
                return render (request, 'app1/signupuser.html', {'form':UserCreationForm(), 'error':'Password did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render (request, 'app1/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render (request, 'app1/loginuser.html', {'form':AuthenticationForm(), 'error':'username or password did not match'})
        else:
            login(request, user)
            return redirect('home')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
