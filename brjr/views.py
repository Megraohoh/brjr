from django.shortcuts import render
from .models import Birthday
from django.http import JsonResponse

def index(request):
	return render(request, 'brjr/index.html')
	
def birthdays(request):
	birthdays = Birthday.objects.all().values()
	birthday_list = list(birthdays)
	return JsonResponse(birthday_list, safe=False)