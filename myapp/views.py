from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "heading": "Welcome to BlogLore",
        "headingX": "BlogLore",
        
        
    }
    return render(request, 'home.html', context)
    

def about(request):
    context = {
        "heading": "BlogLore",
        "headingX" : "About BlogLore"
        
        
        
    }
    return render(request, 'about.html', context)
