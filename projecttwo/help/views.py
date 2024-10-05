from django.shortcuts import render

# Create your views here.
def help(request):
    helpdict = {'helpme':'This is the help page'}
    return render(request,'help/help.html',context=helpdict)