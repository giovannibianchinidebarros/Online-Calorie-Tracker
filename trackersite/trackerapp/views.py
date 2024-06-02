from django.shortcuts import render, redirect
from .models import Food, Consume
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index(request):

    foods = Food.objects.all()

    if request.user.is_authenticated:
        consumed_items = Consume.objects.filter(user=request.user)

    if request.method == 'POST':
        if 'add_consume' in request.POST:
            user = request.user
            food_consumed_id = request.POST.get('food_consumed')
            food_consumed = Food.objects.get(id=food_consumed_id)

            consume = Consume(user=user, food_consumed=food_consumed)
            consume.save()

        elif 'remove_consume' in request.POST:
            consume_id = request.POST.get('consume_id')
            consumed_food = Consume.objects.get(id=consume_id)
            consumed_food.delete()
            return redirect('index')

        elif 'remove_all_consume' in request.POST:
            Consume.objects.all().delete()
            return redirect('index')

    return render(request, "trackerapp/index.html", {'foods': foods, 'consumed_items': consumed_items})
