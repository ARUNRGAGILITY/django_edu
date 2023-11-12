from django.shortcuts import render

# Create your views here.
app_name = "app_web"

def home_page(request):
    # take inputs
    # process inputs
    
    # send outputs (info, template, request)
    context = {
        'page': 'home',
    }
    template_file = f"{app_name}/app_web_home.html"
    return render(request, template_file, context)


def about_page(request):
    # take inputs
    # process inputs
    
    # send outputs (info, template, request)
    context = {
        'page': 'about',
    }
    template_file = f"{app_name}/about.html"
    return render(request, template_file, context)

def contact_us_page(request):
    # take inputs
    # process inputs
    
    # send outputs (info, template, request)
    context = {
        'page': 'contact',
    }
    template_file = f"{app_name}/contact_us.html"
    return render(request, template_file, context)