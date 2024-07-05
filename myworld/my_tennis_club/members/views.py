from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

# Create your views here.
def members(request):
    # template = loader.get_templates('myfirst.html')
    # return HttpResponse(template.render())
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))
"""
The details view does the following:
Gets the id as an argument.
uses the id to locate the correct 
"""
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
"""
    The main view does the following:
    loads the main.html template
    Output the html that is rendered by the template
"""
def testing(request):
    # mymembers=Member.objects.filter(Q(firstname='Vinit')|Q(lastname='Pal')).values()
    # mymembers=Member.objects.all().order_by('firstname')
    mymembers=Member.objects.all().order_by('firstname')
    print(mymembers)
    template=loader.get_template('template.html')
    context = {
        'mymembers' : mymembers
    }
    return HttpResponse(template.render(context, request))

# def myf(request):
#     return render(request,'myfirst.html')
    