from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import Context
from django.views.generic.base import TemplateView
from article.models import Article

# Create your views here.
def home(request):
	return render(request,"home.html")

def hello(request):
	name = "CDan"
	html = "<html><body>Hi %s,Seems to be working!</body></html>"% name
	return HttpResponse(html)

def hello_template(request):
	name = "CDan"
	t = get_template('hello.html')
	html = t.render(Context({'name':name}))
	return HttpResponse(html)

def hello_template_simple(request):
	name ="CDan"
	return render_to_response('hello.html',{'name':name})

class HelloTemplate(TemplateView):

	template_name = 'hello_class.html'

	def get_context_data(self, **kwargs):
		context = super(HelloTemplate, self).get_context_data(**kwargs)
		context['name'] = 'CDan'
		return context

def poll(request):
	return render_to_response('poll.html',
		                      {'poll':Article.objects.all()})

def polls(request,polls_id=1):
	return render_to_response('polls.html',
		                      {'polls':Article.objects.get(id=polls_id)})
		