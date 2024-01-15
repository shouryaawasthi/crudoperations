from django.shortcuts import render
from .models import students
from django.contrib import messages


def index(request):
    student_list = students.objects.all()
    
    if request.method == "POST":
        if "add" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            students.objects.create(
                name=name,
                email=email
            )
            messages.success(request, 'Student added successfully')

        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")

            try:
                update_student = students.objects.get(id=id)
                update_student.name = name
                update_student.email = email
                update_student.save()
                messages.success(request, "Student updated successfully")
            except students.DoesNotExist:
                messages.error(request, "Student does not exist")
            
        elif "delete" in request.POST:
            id = request.POST.get("id")
            students.objects.get(id=id).delete()
            messages.success(request, "Student deleted successfully")

      

    data = {"a": student_list}
    return render(request, "index.html", data)

