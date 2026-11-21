from django.shortcuts import render, redirect, get_object_or_404
from . models import Employee
# Create your views here.

# Employee list
def employee_list(request):
    employee = Employee.objects.all()
    return render(request, 'employee_list.html', {'employee':employee})

#add employee view
def create_employee(request):
    if request.method == 'POST':
        Employee.objects.create(
            name=request.POST.get('name'),
            email = request.POST.get('email'),
            dept = request.POST.get('dept'),
            salary = request.POST.get('salary')
        )

        return redirect('employee_list')
    return render(request, 'employee_form.html')


# employee detail 
def employee_details(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detils.html', {'employee':employee})

#update employee view
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk = pk)
    if request.method == 'POST':
        employee.name=request.POST.get('name').strip() #strip for remove unwanted space
        employee.email = request.POST.get('email').strip()
        employee.dept = request.POST.get('dept'.strip())
        employee.salary = request.POST.get('salary')

        employee.save()
        return redirect('employee_list')
    return render(request, 'update_employee.html', {'employee':employee})

#delete employee view
def delete_employee(request, pk):
    employee = get_object_or_404(Employee,pk=pk)
    if request.method== 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'delete_employee.html', {'employee':employee})