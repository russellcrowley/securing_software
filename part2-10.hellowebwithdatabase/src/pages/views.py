from django.http import HttpResponse
from .models import Message


# Create your views here.

def homePageView(request):
	db_id = request.GET.get('id')
	first = Message.objects.get(id = db_id)
	content = first.content
	
	return HttpResponse(content)
