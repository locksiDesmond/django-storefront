from django.shortcuts import render
from django.http import HttpResponse

def calculate():
	x = 1
	y = 3
	return x +y
# Create your views here.
def say_hello(request): 
	x = calculate()
	print(x)
	return render(request, 'hello.html' )