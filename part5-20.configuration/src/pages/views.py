from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Account


@login_required
def transferView(request):
	
	if request.method == "POST":
		to = User.objects.get(username=request.POST.get('to'))
		amount = int(request.POST.get('amount'))

		acc1 = Account.objects.get(user = request.user)
		acc2 = Account.objects.get(user = to)

		if amount <0:
			return

		if acc1.balance < amount:
			return

		acc1.balance -= amount
		acc2.balance += amount

		acc1.save()
		acc2.save()

	return redirect('/')


@login_required
def homePageView(request):
	accounts = Account.objects.exclude(user_id=request.user.id)
	return render(request, 'pages/index.html', {'accounts': accounts})
