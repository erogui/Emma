from django.shortcuts import render

def index(request):
	return render(request, 'presentation/home.html')
