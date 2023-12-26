from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from Rezume.forms import UserRegistrationForm
from .models import Contact , Resume,Potfolio,Testomonial,Education,Service,Post

# Create your views here.
class Homepage(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['service_data']= Service.objects.all()
      context['post_data']= Post.objects.all()
      return context

def contact(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        msg = request.POST['message']

        contact = Contact(name=name, email=email, message=msg)
        contact.save()
        return HttpResponse('Thanks for your response')
        # Contact.objects.create(name=name, email=email, message=msg)

    else:
        form= UserRegistrationForm()
        return render(request,'contact.html',context={'form':form})

# def About(request):
#     return render(request,'about.html')

# def Portfolio(request):
#     return render(request,'portfolio.html')
class About(ListView):
    test = Testomonial.objects.all()
    model = Testomonial
    template_name = 'about.html'
class Resumee(TemplateView):
    template_name = 'resume.html'
    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['resume_data']= Resume.objects.all()
      context['education_data']= Education.objects.all()
      return context


class Portfolioo(ListView):
    ab =Potfolio.objects.all()
    model = Potfolio
    template_name = 'portfolio.html'

def Blogpost(request ,pk):
    cv = Post.objects.get(id=pk)
    return render(request,'detail.html', {'post':cv})