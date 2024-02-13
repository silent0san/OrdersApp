from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DishForm
from Orders_Project.orders_App.models import OrderedDish
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Sum

def home(request):
    return render(request, 'orders_App/home.html')


@login_required(login_url='/login')
def my_order(request):
    submitted = False
    current_logged_user = request.user.username
    all_dishes = OrderedDish.objects.all().order_by('created_date').filter(owner=current_logged_user)
    to_pay = OrderedDish.objects.filter(owner=current_logged_user).aggregate(Sum('price'))

    if request.method == "POST":
        form = DishForm(request.POST)
        if form.is_valid():
            saved_form_data = form.save(commit=False)
            saved_form_data.owner = current_logged_user
            form.save()
            return redirect("/my_order")
    else:
        form = DishForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'orders_App/my_order.html', {"form": form, 'submitted': submitted, 'all_dishes': all_dishes})


def group_order(request):
    all_dishes = OrderedDish.objects.all().order_by('created_date')
    to_pay = OrderedDish.objects.aggregate(Sum('price'))
    return render(request, 'orders_App/group_order.html', {'all_dishes': all_dishes})


@login_required(login_url='/login')
def delete_dish(request, dish_id):
    dish = get_object_or_404(OrderedDish, pk=dish_id)
    if request.user.username == dish.owner:
        dish.delete()

        return redirect('/my_order')
    else:
        return HttpResponse('No permissions')
