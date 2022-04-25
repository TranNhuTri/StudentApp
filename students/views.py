from django.shortcuts import render
from .forms import StudentForm
from .models import Student
# Create your views here.
def create_view(request):
    if request.method == "POST":
        new_code = request.POST.get("code")
        print(new_code)
        
    context = {}
    return render(request, 'create.html', context)

# def create_view(request):
#     form = StudentForm(request.POST or None)
#     if form.is_valid():
#         form.save()
    
#     context = {
#         'form': form
#     }
#     return render(request, 'create.html', context)

def detail_view(request):
    student = Student.objects.get(id=1)
    context = {
        'student': student
    }
    return render(request, 'detail.html', context)