from django.shortcuts import render

# Create your views here.

def addPageView(request):
	items = request.session.get('items', [])
	if request.method == 'POST':
		item = request.POST.get('content', '').strip()
		if len(items) < 10:
			items.append(item)
		else:
			items.pop(0)
			items.append(item)
	print(items)
	request.session['items'] = items

	# shorter way of writing instead of loader
	return render(request, 'pages/index.html', {'items' : items})



def erasePageView(request):
	items = request.session.get('items', [])
	items.clear()
	request.session['items'] = items
	return render(request, 'pages/index.html', {'items' : items})


def homePageView(request):
	# use sessions (the data is stored in a database db.sqlite that is then accessed using a cookie)
	items = request.session.get('items', [])
	# shorter way of writing instead of loader
	return render(request, 'pages/index.html', {'items' : items})
