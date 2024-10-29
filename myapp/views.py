from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required  # This will ensure that only authenticated users can access this view
def home_view(request):
    return render(request, 'home.html')