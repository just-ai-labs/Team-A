#This file holds all the variables which are used globally

project_id = 20241 #Name of the project acts as ID and can be incremented
project_file = str(project_id)+'.txt' #The text file path
user_responses = [] #Stores the user sentiments based on their responses
request_response = {} #A dictionary which holds every conversation between agent and user. The conversation from agent is stored as key and that of the user is stored as value to that key.
k=0 #A variable to guide the global level indexing.
charter_input = {}
frd_input = {}
updates = []
complete = 0

#Set of first half of the enquiry questions. Created to randomize the sentences. It works with the help of utility.gen_random() function to get an index.
question_lines_1 = [
    "Do you have any input on ",
    "Is there anything you'd like to share about ",
    "Would you care to elaborate on ",
    "Can you provide any details about ",
    "Is there something you'd like to mention about ",
    "Would you like to contribute any information on ",
    "Do you have anything specific to add regarding ",
    "Could you share more about ",
    "Is there any particular insight you’d like to provide on ",
    "Would you like to discuss anything about "
]
#Set of second half of the enquiry questions. Created to randomize the sentences. It works with the help of utility.gen_random() function to get an index.
question_lines_2 = [
    ", especially regarding",
    ", particularly focusing on ",
    ", specifically on ",
    ", especially related to ",
    ", particularly concerning ",
    ", especially about ",
    ", particularly in relation to ",
    ", with an emphasis on ",
    ", especially on ",
    ", especially in terms of "
]