from django.shortcuts import render, get_object_or_404
from django.contrib import admin
from .models import Course

# Create your views here.
def index(request):
	courses= Course.objects.all()
	template_index= 'courses/index.html'
	context= {
			'courses':courses
	}
	return render(request, template_index, context)

#def details(request,pk):
#	course= get_object_or_404(Course, pk=pk)
#	context={
#		'course': course
#	}
#	template_name= 'courses/details.html'
#	return render(request, template_name, context)

def details(request,slug):
	course= get_object_or_404(Course, slug=slug)
	context={
		'course': course
	}
	template_name= 'courses/details.html'
	return render(request, template_name, context)