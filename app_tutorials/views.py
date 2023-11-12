from django.shortcuts import render


app_name = "app_tutorials"
def tutorials_home_page(request):
    #
    
    
    
    #
    context = {
        'page': "tutorials",
    }
    template_file = f"{app_name}/tutorials_home.html"
    return render(request, template_file, context)
