from django.http import HttpResponse


# Create your views here.

def addPageView(request):
	first = request.GET.get('first')
	second = request.GET.get('second')
	ans = int(first) + int(second)
	return HttpResponse(ans)
	

def multiplyPageView(request):
	first = request.GET.get('first')
	second = request.GET.get('second')
	ans = int(first) * int(second)
	return HttpResponse(ans)
