from django.shortcuts import render
from appone.models import User

# Create your views here.
def index(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, "appone/index.html", context)
    
