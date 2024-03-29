from django.shortcuts import render
from collections import Counter
import configparser
import json
import platform 
import re
app_name = "app_quiz"

### Utility function
def check_two_list(got_list, ref_list):
    ref_answer = [1, 2]  # Reference list of answers
    got_answer = [2, 1]  # List of answers given by the user (different order)
    ref_answer = ref_list
    got_answer = got_list
    # Use Counter to count elements in both lists
    ref_answer_counter = Counter(ref_answer)
    got_answer_counter = Counter(got_answer)

    match_result = False
    # Check if the counters are equal
    if ref_answer_counter == got_answer_counter:
        print("The answers match (ignoring order).")
        match_result = True
    else:
        print("The answers do not match.")
    return match_result


def quiz_home_page(request):
    # take inputs
     
    # process inputs
    
    # send outputs / information
    context = {
        'page': "quiz",
    }
    template_file = f"{app_name}/quiz_home.html"
    return render(request, template_file, context)
def parse_ini_file(file_path):
    questions = {}
    current_section = None
    current_key = None
    multiline = False

    with open(file_path, 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            if line.startswith('[') and line.endswith(']'):
                current_section = line.strip('[]')
                questions[current_section] = {}
            elif '=' in line and not multiline:
                current_key, value = line.split('=', 1)
                current_key = current_key.strip().lower()
                value = value.strip()
                if value.startswith('"""'):
                    multiline = True
                    questions[current_section][current_key] = value[3:] + '\n'
                else:
                    questions[current_section][current_key] = value
            elif multiline:
                if line.endswith('"""'):
                    questions[current_section][current_key] += line[:-3]
                    multiline = False
                else:
                    questions[current_section][current_key] += line + '\n'
    return questions

def show_quiz(request, topic):
    #
    # Define the path to the INI file based on the requested topic
    #f"app_tutorials/templates/app_tutorials/md_content/{topic}.md"
    os_info = platform.system()
    #print(f">>> === OS INFO: {os_info} === <<<")
    prod_path = ""
    if os_info.find("Linux") != -1:
        prod_path = f"/home/DEVAGILEAGILITY/com_learnpythondjango/lpdcom/django_edu/"
    
    ini_file_path = f"{prod_path}{app_name}/templates/{app_name}/quiz_content/{topic}.ini"

    # Read the INI file and parse it
    config = parse_ini_file(ini_file_path)
    # Convert the parsed data into a format suitable for the template
    ####print(f">>> === config {config} === <<<")
    questions = []
    for item in config:
        # Extract the last numeric digit from the section name
        section_number = ''.join(filter(str.isdigit, item))
        #print(f">>> === item {item} === <<<")
        question = config[f'{item}']
        options = question[f'options{section_number}'].split('; ')    
        correct_answer = question[f'correctanswer{section_number}']  
        qno = section_number 
        
        mcq = "scq"  
        if correct_answer.find(',') != -1:
            mcq = "mcq"      
            #print(f">>> === {qno} {question} {mcq} === <<<")       
        question = {
            'question': [qno, question],
            'options': [qno, mcq, options],
            'correct_answer': correct_answer,
            'mcq': mcq,
            'qno': qno,
        }        
        questions.append(question)
    
    # User submits the quiz: processing starts
    if request.method == "POST":
        submitted_answers = {}
        answers = {}
        user_results = {}
        for question in questions:
            options = question['options']
            cq = options[1]
            qno = options[0]
            skey = f"{cq}_{qno}"
            answer_list = question['correct_answer']
            submitted_answers[skey] = None
            answers[skey] = answer_list
            user_results[skey] = 0
        for key, value in request.POST.items():
            if key.startswith("scq_"):
                print(f">>> === SCQ {key} {value} === <<<")
                question_number = key.split("_")[1]
                option_number = value.split("_")[2]
                option_value = value         
                submitted_answers[key] = option_value
            if key.startswith("mcq_"):
                print(f">>> === MCQ {key} {value} === <<<")
                question_number = key.split("_")[1]
                option_number = value.split("_")[2]
                option_value = request.POST.getlist(key)   
                submitted_answers[key] = option_value
        
        ## Calculate the score
        score = 0
        
        for question in questions:
            ref_question = question['question']
            options = question['options']
            cq = options[1]
            qno = options[0]
            skey = f"{cq}_{qno}"
            answer_list = question['correct_answer']
            user_answers = submitted_answers[skey]           
            print(f">>> === {ref_question} === <<<")
            if skey.startswith("scq_") and submitted_answers[skey] != None:
                # user answers are in user_answers
                # reference answers are in answer_list
                got_answer = user_answers.split("_")[2]
                ref_answer = answer_list
                result = False
                if ref_answer == got_answer:
                    result = True
                    user_results[skey] = 1

                print(f">>> === [[CHECKING]] ref_answer {ref_answer} == {got_answer} ..{result}.. got_answer === <<<")
                
            if skey.startswith("mcq_") and submitted_answers[skey] != None:
                # user answers are in user_answers
                # reference answers are in answer_list
                got_answer = [x.split('_')[-1] for x in user_answers]                
                ref_answer = answer_list.split(',')
                result = check_two_list(got_answer, ref_answer)
                if result == True:
                    user_results[skey] = 1            
                #print(f">>> === [[CHECKING]] ref_answer {ref_answer} == {got_answer} ..{result}.. got_answer === <<<")
        
            score += user_results[skey]
            total = len(questions)
            percentage = round((score/total)*100,2)
        context = {'questions': questions,
                'page': 'quiz',
                'quiz_name': topic,
                'answers': submitted_answers,
                'ref_answers': answers,
                'user_results': user_results,
                'score': score,
                'total': total,
                'percentage': percentage,}
        template_file = f"{app_name}/quiz_results.html"
        return render(request, template_file, context )
        
    context = {'questions': questions,
               'page': 'quiz',
               'quiz_name': topic}
    print(f">>> === Questions: {questions} === <<<")
    template_file = f"{app_name}/show_quiz.html"
    return render(request, template_file, context )
    



