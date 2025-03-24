#This is the main file to initiate the Agent

#Importing the requirements
import template
import utility #All the functionalities
import variables #All the variables
import os
import asyncio
complete = 0 #A flag, sets when the conversation completes
#The first approach made to start the conversation


request = f"Hi {utility.greeter()} <USER>, welcome to agent 1. I can help you with creating project charter and flowcharts."
print(request)
response = input()
variables.request_response.update({request: response})

#Sentiment analysis of the user
sys_msg = '''
    If the input expresses a greeting, such as "Hi," "Hello," or has a similar meaning, assign the context as greeting.
If the input is an inquiry, such as "How are you?" or any expression asking about someone's well-being, assign the context as enquiry.
If the input requests help related to starting a project or has a similar meaning, assign the context as project.
If the input is anything else than the mentioned above or if the input is an inquiry such as "what is your age?" or any expression asking the personal questions like age, salary or anything similar except the name, then assign the context as none.
If the input fits into more than one category, concatenate the respective contexts
    '''
variables.user_responses.append (utility.ask_gpt(sys_msg, response))
print('--------------------------------------------------------------')

#A loop which converse with the user until he asks regarding a project
while response:
    variables.request_response.update({request: response})
    variables.user_responses.append(utility.ask_gpt(sys_msg, response))
    if variables.user_responses[-1] == 'greeting':
        request = 'How can I help you?'
        print('How can I help you?')
    elif variables.user_responses[-1] == 'greeting, enquiry' or variables.user_responses[-1] == 'enquiry':
        request = "I'm doing great, Thank you. How can I help you?"
        print("I'm doing great, Thank you. How can I help you?")
    elif variables.user_responses[-1] == 'greeting, enquiry, project' or variables.user_responses[-1] == 'enquiry, project':
        request = "I'm doing great, Thank you. Let's start the project. How do you want to provide the details?"
        print("I'm doing great, Thank you. Let's start the project. How do you want to provide the details?")
        variables.request_response.update({request: response})
        break
    elif variables.user_responses[-1] == 'project' or variables.user_responses[-1] == 'greeting, project':
        request = "Let's start the project.How do you want to provide the details?"
        print("Let's start the project. How do you want to provide the details?")
        print('1.Type directly\t2.Upload document')
        response = input()
        variables.request_response.update({request: response})
        break
    else:
        request = 'I can only help with the project charter and flowchart generation'
        print("What you're asking might be beyond my scope, as I can assist primarily with project charters and flowchart generation")
    print('--------------------------------------------------------------')
    variables.request_response.update({request: response})
    variables.user_responses.append(utility.ask_gpt(sys_msg, response))
    variables.k+=1
    response = input()

#Gets the user choice of providing information.
user_choice = utility.update_user_choice(int(response))

#Further responses of agent based on the user choice of providing information.
if user_choice == 0:
    request = "Great choice. Kindly write the details here"
    print(request)
    response = input()
    print('--------------------------------------------------------------')
    variables.request_response.update({request: response})
    utility.record_response(response)
else:
    request = "Great choice. Kindly drop here"
    print(request)
    path1 = 'H:\\pm\\uploads' # location of the file where the user uploaded files are stored
    ls = os.listdir(path1)
    path2 = ls[-1]
    path = path1 + '\\' + path2
    text = utility.option_2(path)
    print('Processing ')
    sys_msg = '''
    Find the punctuality and spacing in the given text and return the corrected in string format. Do not manipulate any information
    '''
    text = utility.ask_gpt(sys_msg, text)
    utility.record_response(text.strip())

missing_fields = utility.text_analysis(template.template)
print(missing_fields)

#Requirement loop begins:
while len(missing_fields)>0:
    missing_fields, end_convo = utility.response_analysis(missing_fields)
    print(missing_fields)
    if end_convo == 1:
        break
    if len(missing_fields) == 1:
        missing_fields = utility.text_analysis(template.template)
    missing_fields = utility.text_analysis(missing_fields)              # Requirement loop ends

charter_input = utility.text_extraction()
charter = utility.generate_charter(charter_input)
charter.create_project_charter(f"{variables.project_id}charter.docx")
print('Charter created')

frd_input = utility.frd_extraction()
frd = utility.generate_frd(frd_input)
frd.create_frd(f"{variables.project_id}frd.docx")
print('FRD created')
print(variables.frd_input)