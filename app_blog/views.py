from django.shortcuts import render


app_name = "app_blog"
def blog_home_page(request):
    #
    
    
    
    #
    context = {
        'page': "blog",
    }
    template_file = f"{app_name}/blog_home.html"
    return render(request, template_file, context)
