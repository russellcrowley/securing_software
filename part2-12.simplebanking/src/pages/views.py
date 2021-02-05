from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account
from django.db.models import Q
import json



@login_required
def addView(request):
	if request.method == 'POST':
		new_iban = request.POST.get('iban')
		owner = request.user
		new_account = Account.objects.create(owner = request.user, iban = new_iban)
		new_account.save()
	return redirect('/')


@login_required
def homePageView(request):
	accounts = Account.objects.filter(owner=request.user)
	context = {'accounts': accounts}
	return render(request, 'pages/index.html', context)
