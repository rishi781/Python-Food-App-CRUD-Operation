from django.shortcuts import render, redirect
from .models import FoodMenu
from .forms import FoodMenuForm

# Create your views here.


app_name = 'foodapp'
def home(request):
    data = FoodMenu.objects.all()
    return render(request, 'foodapp/home.html', {'items' : data})

def details(request, id):
    data = FoodMenu.objects.get(pk = id)
    return render(request, 'foodapp/details.html', {'items' : data})

def additem(request):
    form = FoodMenuForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("foodapp:home")
    return render(request, 'foodapp/additemForm.html', {'form': form})

def update_item(request,id):
    data = FoodMenu.objects.get(pk=id)
    form= FoodMenuForm(request.POST or None, instance= data)
    if form.is_valid():
        form.save()
        return redirect('foodapp:home')
    return render(request,'foodapp/additemForm.html', {'form': form})

def delete_item(request,id):
    data = FoodMenu.objects.get(pk=id)
    if request.method=='POST':
        data.delete()
        return redirect('foodapp:home')
    return render(request,'foodapp/delete_msg.html', {'items': data})

# 'rows':data key value pair

