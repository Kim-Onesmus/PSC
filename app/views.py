from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, 'app/index.html')


def About(request):
    return render(request, 'app/about.html')

def CoreValues(request):
    return render(request, 'app/core_values.html')

def AreasofInterests(request):
    return render(request, 'app/areas_of_interests.html')

def WhyUs(request):
    return render(request, 'app/why_us.html')

def Leadership(request):
    return render(request, 'app/leadership.html')

def Contact(request):
    return render(request, 'app/contact.html')