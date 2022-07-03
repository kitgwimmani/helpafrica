from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import Content, Member, Support
# Create your views here.
from django.http import HttpResponseRedirect
from .forms import MemberForm
from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        "content": Content.objects.filter(category = 'event'),
        "news": Content.objects.filter(category='news').order_by('-id')
    }
    template = "main/index.html"
    return render(request, template, context)
#@login_required
def add_member(request):
    submitted = False
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_member?submitted=True')
    else:
        form = MemberForm
        if submitted in request.GET:
            submitted = True
    template = "main/register.html"
    form = MemberForm
    return render(request, template, {'form':form, 'submitted':submitted})

#@login_required(login_url='/admin')
def printid(request):
    context = {
        "member": Member.objects.all(),
    }
    template = "main/printid.html"
    return render(request, template, context)

def gallery(request):
    context = {
        "gallery": Content.objects.filter(category='gallery').order_by('-id')
    }
    template = "main/gallery.html"
    return render(request, template, context)

def event(request):
    context = {
        "event": Content.objects.filter(category='event').order_by('-id')
    }
    template = "main/event.html"
    return render(request, template, context)

def about(request):
    context = {
    }
    template = "main/about.html"
    return render(request, template, context)

def donate(request):
    context = {
         "support": Support.objects.all().order_by('-id')
    }
    template = "main/donate.html"
    return render(request, template, context)