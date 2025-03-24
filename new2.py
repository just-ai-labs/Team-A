import json
import re
import openai
import os
from dotenv import load_dotenv
from create_brd_doc import create_brd_document

# Load environment variables
load_dotenv()

# Configure OpenAI API
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("No API key found. Please check your .env file.")
openai.api_key = api_key

def read_charter_file(file_path):
    """Read content from charter.txt"""
    with open(file_path, 'r') as file:
        return file.read()

def convert_to_json_structure(text):
    """Convert the text response to proper JSON structure"""
    sections = {
        'Executive Summary': '',
        'Project Objectives': {
            'Specific': '',
            'Measurable': '',
            'Achievable': '',
            'Relevant': '',
            'Time-specific': ''
        },
        'Project Scope': {
            'Timeline': '',
            'Budget': '',
            'Deliverables': '',
            'Project Requirements': '',
            'Project Team': ''
        },
        'Business Requirements': '',
        'Key Stakeholders': [],  # Changed to list
        'Project Constraints': {
            'Project Risks': '',
            'Team Availability': '',
            'Resources': '',
            'Project Dependencies': '',
            'Deadlines': '',
            'Project Budget': ''
        },
        'Cost-Benefit Analysis': []  # Changed to list
    }
    
    current_section = None
    current_subsection = None
    buffer = []
    
    lines = text.strip().split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if it's a main section
        if line.endswith(':'):
            # Process previous buffer if exists
            if buffer and current_section:
                if isinstance(sections[current_section], list):
                    sections[current_section].extend([item.strip('• ') for item in buffer])
                elif current_subsection and isinstance(sections[current_section], dict):
                    sections[current_section][current_subsection] = '\n'.join(buffer)
                else:
                    sections[current_section] = '\n'.join(buffer)
                buffer = []
                
            current_section = line[:-1].strip()
            current_subsection = None
            continue
            
        # Handle subsections
        if line.startswith('-'):
            line = line[1:].strip()
            if ':' in line:
                # Process previous buffer
                if buffer and current_subsection:
                    sections[current_section][current_subsection] = '\n'.join(buffer)
                    buffer = []
                    
                key, value = line.split(':', 1)
                current_subsection = key.strip()
                if value.strip():
                    buffer.append(value.strip())
            continue
            
        # Add content to buffer
        if line.startswith('•'):
            line = line.strip('• ')
        buffer.append(line)
    
    # Process final buffer
    if buffer and current_section:
        if isinstance(sections[current_section], list):
            sections[current_section].extend([item.strip('• ') for item in buffer])
        elif current_subsection and isinstance(sections[current_section], dict):
            sections[current_section][current_subsection] = '\n'.join(buffer)
        else:
            sections[current_section] = '\n'.join(buffer)
            
    return sections

def extract_information(text):
    """Extract key information using OpenAI API"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": """Extract and organize the information into these sections:
                    Executive Summary: (provide a concise overview)
                    
                    Project Objectives:
                    - Specific: (describe specific goals)
                    - Measurable: (define measurable outcomes)
                    - Achievable: (outline achievable targets)
                    - Relevant: (explain business relevance)
                    - Time-specific: (specify timeframes)
                    
                    Project Scope:
                    - Timeline: (specify duration)
                    - Budget: (state total budget)
                    - Deliverables: (list key deliverables)
                    - Project Requirements: (list requirements)
                    - Project Team: (specify team structure)
                    
                    Business Requirements: (detail business needs)
                    
                    Key Stakeholders: (list all stakeholders with bullet points)
                    
                    Project Constraints:
                    - Project Risks: (identify risks)
                    - Team Availability: (specify resource availability)
                    - Resources: (list required resources)
                    - Project Dependencies: (identify dependencies)
                    - Deadlines: (specify key dates)
                    - Project Budget: (detail budget constraints)
                    
                    Cost-Benefit Analysis: (list benefits with bullet points)
                    
                    Use bullet points (•) for lists and clear section headers with colons."""
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            temperature=0.0,
            max_tokens=1500
        )
        
        extracted_content = response.choices[0].message['content']
        structured_data = convert_to_json_structure(extracted_content)
        return json.dumps(structured_data, indent=2)
        
    except Exception as e:
        return f"Error in API call: {str(e)}"

def main():
    # First part: Create JSON file
    charter_path = "Sample_text.txt"
    try:
        charter_content = read_charter_file(charter_path)
        extracted_info = extract_information(charter_content)
        
        json_file_path = "extracted_project_scope.json"
        
        # Save extracted information to JSON file
        with open(json_file_path, 'w') as file:
            file.write(extracted_info)
        
        print("Project Information extracted successfully!")

        # Second part: Create Word document
        output_file_path = "Business_Requirements_Document.docx"
        create_brd_document(json_file_path, output_file_path)
        print(f"Document successfully created as {output_file_path}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()