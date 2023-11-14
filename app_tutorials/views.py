from django.shortcuts import render

import os
import platform

app_name = "app_tutorials"
def tutorials_home_page(request):
    #
    
    
    
    #
    context = {
        'page': "tutorials",
    }
    template_file = f"{app_name}/tutorials_home.html"
    return render(request, template_file, context)



def test_markdown(request):
    # File path to the Markdown file in the template directory
    markdown_file_path = 'app_tutorials/templates/app_tutorials/md_content/test_md.md'
    # Read the content of the Markdown file
    html_content = ""
    with open(markdown_file_path, 'r') as file:
        markdown_content = file.read()
    
    context = {'html_content': markdown_content,
               'page': 'tutorials'}
    template_file = f"{app_name}/test_markdown.html"
    return render(request, template_file, context)


def display_md_topic(request, topic):
    os_info = platform.system()
    print(f">>> === OS INFO: {os_info} === <<<")
    prod_path = ""
    if os_info.find("Linux") != -1:
        prod_path = f"/home/DEVAGILEAGILITY/com_learnpythondjango/lpdcom/django_edu/"
    # File path to the Markdown file in the template directory
    markdown_file_path = f"{prod_path}{app_name}/templates/{app_name}/md_content/{topic}.md"
    # Print the file path for debugging
    print(">>> === Markdown file path: {markdown_file_path} === <<<" )
    # Read the content of the Markdown file
    html_content = ""
    with open(markdown_file_path, 'r') as file:
        markdown_content = file.read()
    context = {'html_content': markdown_content,
               'page': 'tutorials',
               'topic': topic,}
    template_file = f"{app_name}/display_md_topic.html"
    return render(request, template_file, context)
