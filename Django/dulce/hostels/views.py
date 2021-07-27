from django.shortcuts import render

# Create your views here.
def hostel_list(request):
    return render(request, 'index.html' )