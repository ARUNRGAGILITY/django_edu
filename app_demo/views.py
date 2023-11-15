from django.shortcuts import render

import os
import platform

app_name = "app_demo"
def demo_home_page(request):
    #
    
    
    
    #
    context = {
        'page': "demo",
    }
    template_file = f"{app_name}/demo_home.html"
    return render(request, template_file, context)



def display_demo_topic(request, topic):
    os_info = platform.system()
    prod_path = ""
    if os_info.find("Linux") != -1:
        prod_path = f"/home/DEVAGILEAGILITY/com_learnpythondjango/lpdcom/django_edu/"
    markdown_file_path = f"{prod_path}{app_name}/templates/{app_name}/md_content/{topic}.md"
    
    # Check if the Markdown file exists
    if not os.path.exists(markdown_file_path):
        # If it doesn't exist, create the file with a simple one-liner content
        with open(markdown_file_path, 'w') as file:
            file.write(f"#{topic}")
    
    html_content = ""
    with open(markdown_file_path, 'r') as file:
        markdown_content = file.read()
    context = {'html_content': markdown_content,
               'page': 'demo',
               'topic': topic,}
    template_file = f"{app_name}/display_demo_topic.html"
    return render(request, template_file, context)
