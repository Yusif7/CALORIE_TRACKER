from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from .models import Food, Consume


def home(request):
    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        return redirect('home')

    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    context = {
        'foods': foods,
        'consumed_food': consumed_food,
    }
    return render(request, 'home.html', context)


def delete(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('home')
    return redirect('home')

