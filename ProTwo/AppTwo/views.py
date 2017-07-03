from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.
def index(request):
    return render(request,'AppTwo/index.html')

def help(request):
    helpdict = {'help_insert':'Help page'}
    return render(request,'AppTwo/help.html',context=helpdict)

def users(request):
    users_list=User.objects.order_by('first_name')
    users_dict={'user_details':users_list}
    return render(request,'AppTwo/users.html',context=users_dict)
