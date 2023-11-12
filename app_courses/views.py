from django.shortcuts import render


app_name = "app_courses"
def courses_home_page(request):
    #
    
    
    
    #
    context = {
        'page': "courses",
    }
    template_file = f"{app_name}/courses_home.html"
    return render(request, template_file, context)
