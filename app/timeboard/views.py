# from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


# Create your views here.
def hello_world(request):
	name = request.GET.get('name')
	result = ''
	if not request.GET.get('name'):
		result = 'Hello, World!'
	else:
		result = 'Hello, ' + name + '!'
	return HttpResponse(result)


class IndexView(generic.TemplateView):
	template_name = 'timeboard/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Tasks'
		return context
