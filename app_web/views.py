from django.shortcuts import render
import os
import platform
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

def display_web_topic(request, topic):
    os_info = platform.system()
    print(f">>> === OS INFO: {os_info} === <<<")
    prod_path = ""
    if os_info.find("Linux") != -1:
        prod_path = f"/home/DEVAGILEAGILITY/com_learnpythondjango/lpdcom/django_edu/"
    # File path to the Markdown file in the template directory
    markdown_file_path = f"{prod_path}{app_name}/templates/{app_name}/md_content/{topic}.md"
    
    # Check if the Markdown file exists
    if not os.path.exists(markdown_file_path):
        # If it doesn't exist, create the file with a simple one-liner content
        with open(markdown_file_path, 'w') as file:
            file.write(f"#{topic}")
    
    # Read the content of the Markdown file
    html_content = ""
    with open(markdown_file_path, 'r') as file:
        markdown_content = file.read()
    context = {'html_content': markdown_content,
               'page': 'home',
               'topic': topic,}
    template_file = f"{app_name}/display_web_topic.html"
    return render(request, template_file, context)