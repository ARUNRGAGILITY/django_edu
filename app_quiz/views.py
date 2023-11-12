from django.shortcuts import render


app_name = "app_quiz"
def quiz_home_page(request):
    #
    
    
    
    #
    context = {
        'page': "quiz",
    }
    template_file = f"{app_name}/quiz_home.html"
    return render(request, template_file, context)
