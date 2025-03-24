from IPython.display import display, HTML
import textwrap
import html
import ast

#extarion of data from charter with ast
def preprocessing(input, number_code):
  if number_code == 1:
    return ast.literal_eval(input)

  if number_code == 2:
    input = input.split('\n')
    return input

def wrap_paragraph(paragraph, line_width=80):
    """Wraps a paragraph to ensure no line exceeds the specified width."""
    return textwrap.fill(paragraph, width=line_width)
# table for risk management.
def create_risk_assessment_table(risk_data):
    """
    Creates a dynamic HTML table with three columns: Department, Rate, and Risk.
    The number of rows depends on the number of lists in the input data.
    Preprocesses the list by converting it to string and then evaluating it using ast.literal_eval.
    """

    # Preprocess the list by converting it to string and then evaluating it using ast.literal_eval
    #risk_data_str = str(risk_data)
    preprocessed_data = ast.literal_eval(risk_data)
    #preprocessed_data = risk_data

    table_html = """
    <table border="1" style="border-collapse: collapse; width: 50%; text-align: left;">
        <thead>
            <tr style="background-color: #d3d3d3;">
                <th>Department</th>
                <th>Rate</th>
                <th>Risk</th>
            </tr>
        </thead>
        <tbody>
    """

    for department, rate, risk in preprocessed_data:
        table_html += f"""
            <tr>
                <td>{html.escape(department)}</td>
                <td>{html.escape(rate)}</td>
                <td>{html.escape(risk)}</td>
            </tr>
        """

    table_html += """
        </tbody>
    </table>
    """
    return table_html

def create_stakeholder_table(stakeholder_data):
    """
    Creates a dynamic HTML table with two columns: Name and Work.
    The number of rows is determined by the length of the input list.
    """
    preprocessed_data = [
        [entry[0].strip().title(), entry[1].strip().capitalize()]
        for entry in stakeholder_data
    ]

    table_html = """
    <table border="1" style="border-collapse: collapse; width: 50%; text-align: left;">
        <thead>
            <tr style="background-color: #d3d3d3;">
                <th>Name</th>
                <th>Work</th>
            </tr>
        </thead>
        <tbody>
    """

    for name, work in preprocessed_data:
        table_html += f"""
            <tr>
                <td>{html.escape(name)}</td>
                <td>{html.escape(work)}</td>
            </tr>
        """

    table_html += """
        </tbody>
    </table>
    """
    return table_html
# for risk owner
def create_risk_owners_table(risk_owners_data):
    """
    Creates a dynamic HTML table with two columns: Lead and Work.
    The number of rows depends on the number of lists in the input data.
    Preprocesses the list by converting it to string and then evaluating it using ast.literal_eval.
    """
    preprocessed_data = ast.literal_eval(risk_owners_data)  # Preprocessing

    table_html = """
    <table border="1" style="border-collapse: collapse; width: 50%; text-align: left;">
        <thead>
            <tr style="background-color: #d3d3d3;">
                <th>Lead</th>
                <th>Work</th>
            </tr>
        </thead>
        <tbody>
    """

    for lead, work in preprocessed_data:
        table_html += f"""
            <tr>
                <td>{html.escape(lead)}</td>
                <td>{html.escape(work)}</td>
            </tr>
        """

    table_html += """
        </tbody>
    </table>
    """
    return table_html




def create_budgetary_table(budgetary_data):
        table_html = """
        <table border="1" style="border-collapse: collapse; width: 50%; text-align: left;">
            <thead>
                <tr style="background-color: #d3d3d3;">
                    <th>Cost</th>
                    <th>Sector</th>
                </tr>
            </thead>
            <tbody>
        """
        for cost, sector in budgetary_data:
            table_html += f"""
                <tr>
                    <td>{html.escape(cost)}</td>
                    <td>{html.escape(sector)}</td>
                </tr>
            """
        table_html += """
            </tbody>
        </table>
        """
        return table_html
# for para
def line(paragraph):
  """Converts a list to a line, replacing commas with 'on'."""
  # Convert list to comma-separated string
  line_str = ','.join(paragraph)
  # Replace commas with 'on'
  line_str = line_str.replace(',', ' on ')
  return line_str

def textpoint(paragraph):
    """
    Converts a paragraph into point-wise format:
    - Replaces commas with full stops.
    - Removes unnecessary brackets and quotation marks.
    - Splits the paragraph into points based on full stops.
    - Each point starts with an arrow symbol (→) and appears on a new line.
    """
    # Replace commas with full stops
    formatted_paragraph = paragraph.replace(",", ".")

    # Remove brackets and strip single/double quotes
    cleaned_paragraph = formatted_paragraph.strip("[]").replace("'", "").replace('"', "")

    # Split the paragraph into points (sentences) by full stops
    points = [f"→ {point.strip()}." for point in cleaned_paragraph.split(".") if point.strip()]
    # Join points with a new line
    return "<br>".join(points)

def display_project_overview(charter_input):
    """Displays the Project Overview information with stakeholder information as a dynamic table."""
    # Preprocessing and wrapping text
    project_name = charter_input['Project Overview']['Project Name']
    project_start = charter_input['Project Overview']['Project Start(projected)']
    project_end = charter_input['Project Overview']['Project End(projected)']
    problem_statement = wrap_paragraph(charter_input['Business Case and Project Objectives']['Problem Statement'])
    goals_and_objectives = wrap_paragraph(charter_input['Business Case and Project Objectives']['Goals and Objectives'])
    expected_benefits = wrap_paragraph(charter_input['Business Case and Project Objectives']['Expected Benefits'])
    strategic_alignment = wrap_paragraph(charter_input['Business Case and Project Objectives']['Strategic Alignment'])

    stakeholder_register = ast.literal_eval(charter_input['Stakeholder Information']['Stakeholder Register'])
    roles_and_responsibilities = wrap_paragraph(charter_input['Stakeholder Information']['Roles and Responsibilities'])
    communication_preferences = wrap_paragraph(charter_input['Stakeholder Information']['Communication Preferences'])
    scope_statement = wrap_paragraph(charter_input['Project Scope']['Scope Statement'])
    deliverables = wrap_paragraph(charter_input['Project Scope']['Deliverables'])
    boundaries_and_constraints = wrap_paragraph(charter_input['Project Scope']['Boundaries and Constraints'])
     #   'Requirements Documentation': ['Functional Requirements', 'Non-functional Requirements', 'Compliance Requirements', 'Risk Considerations']
    Functional_Requirements = textpoint(charter_input['Requirements Documentation']['Functional Requirements'])
    Non_functional_Requirements = textpoint(charter_input['Requirements Documentation']['Non-functional Requirements'])
    communication_preferences = textpoint(charter_input['Requirements Documentation']['Compliance Requirements'])
    Risk_Considerations = ast.literal_eval(charter_input['Requirements Documentation']['Risk Considerations'])
    # 'Resources': ['Human Resources', 'Physical Resources', 'Budgetary Information']
    Human_Resources = textpoint(charter_input['Resources']['Human Resources'])
    Physical_Resources = textpoint(charter_input['Resources']['Physical Resources'])
    Budgetary_Information = ast.literal_eval(charter_input['Resources']['Budgetary Information'])
    #'Risk Assessment': ['Initial Risk Register', 'Mitigation Strategies', 'Risk Owners']
    risk_register = charter_input['Risk Assessment']['Initial Risk Register']
    Mitigation_Strategies = textpoint(charter_input['Risk Assessment']['Mitigation Strategies'])
    risk_owners = charter_input['Risk Assessment']['Risk Owners']  # Extract risk owners data

    #'Methodology and Tools': ['Selected Project Management Methodology', 'Tools', 'Reporting Format and Frequency']
    Selected_Project_Management_Methodology = textpoint(charter_input['Methodology and Tools']['Selected Project Management Methodology'])
    Tools = textpoint(charter_input['Methodology and Tools']['Tools'])
    Reporting_Format_and_Frequency = textpoint(charter_input['Methodology and Tools']['Reporting Format and Frequency'])
    #'Approval and Governance': ['Project Charter Approval', 'Executive Sponsor Sign-Off', 'Governance Model']
    Project_Charter_Approval = ast.literal_eval(charter_input['Approval and Governance']['Project Charter Approval'])
    Executive_Sponsor_Sign_Off = ast.literal_eval(charter_input['Approval and Governance']['Executive Sponsor Sign-Off'])
    Governance_Model = textpoint(charter_input['Approval and Governance']['Governance Model'])

    # Generate Stakeholder Table HTML
    stakeholder_table = create_stakeholder_table(stakeholder_register)
    risk_table = create_risk_assessment_table(risk_register)  # Create risk table HTML
    budgetary_table = create_budgetary_table(Budgetary_Information)
    risk_owners_table = create_risk_owners_table(risk_owners)  # Create risk owners table HTML
    Project_Charter_Approval = line(Project_Charter_Approval)
    Executive_Sponsor_Sign_Off = line(Executive_Sponsor_Sign_Off)
    html_content = f"""
    <u><h1><b><div style=" text-align: center;">Project Charter</div></b></h1></u><br>
    <div style="font-size: 15px; margin-bottom: 20px; text-decoration: none;padding: 5px 10px; background-color: lightblue; display: inline-block;width: fit-content; min-width: 6in; border-radius: 10px;">
    <h3><b>Project Overview</b></h3>
</div>
    </div><br>
    <p><b>Project Name:</b> {project_name}</p>
    <p><b>Project Start(projected):</b> {project_start}</p>
    <p><b>Project End(projected):</b> {project_end}</p>
    <div style="padding: 0px; background-color: lightblue; display: inline-block; width: 6in;">
        <h3><b>Business Case And Project Objective</b></h3>
    </div><br>
    <p><b>Problem Statement:<br></b> {problem_statement}</p>
    <p><b>Goals And Objectives:<br></b> {goals_and_objectives}</p>
    <p><b>Expected Benefits:<br></b> {expected_benefits}</p>
    <p><b>Strategic Alignment:<br></b> {strategic_alignment}</p>
    <div style="border: 2px solid blue; padding: 10px; background-color: lightblue; display: inline-block; width: 8in;">
        <h3><b>Stakeholder Information</b></h3>
    </div><br>
    <p><b>Stakeholder Register:</b></p>
    {stakeholder_table}
    <p><b>Roles and Responsibilities:<br></b>{roles_and_responsibilities}</p>
    <p><b>Communication Preferences:<br></b>{communication_preferences}</p>
    <div style="border: 2px solid blue; padding: 10px; background-color: lightblue; display: inline-block; width: 8in;">
        <h3><b>Project Scope</b></h3>
    </div><br>
    <p><b>Scope Statement:<br></b>{scope_statement}</p>
    <p><b>Deliverables:<br></b>{deliverables}</p>
    <p><b>Boundaries and Constraints:<br></b>{boundaries_and_constraints}</p>
    <div style="border: 2px solid blue; padding: 10px; background-color: lightblue; display: inline-block; width: 8in;">
        <h3><b>Requirement Document</b></h3>
    </div><br>
    <p><b>Functional Requirements:<br></b>{Functional_Requirements}</p>
    <p><b>Non-functional Requirements:<br></b>{Non_functional_Requirements}</p>
    <p><b>Compliance Requirements:<br></b>{communication_preferences}</p>

    <div style="border: 2px solid blue; padding: 10px; background-color: lightblue; display: inline-block; width: 8in;">
        <h3><b>Resources</b></h3>
    </div><br>
    <p><b>Human Resources:<br></b>{Human_Resources}</p>
    <p><b>Physical Resources:<br></b>{Physical_Resources}</p>
    <p><b>Budgetary Information:<br></b>{budgetary_table}</p>
    <div style="border: 2px solid blue; padding: 10px; background-color: lightblue; display: inline-block; width: 8in;">
        <h3><b>Risk Assement</b></h3>
        </div><br>

      <p><b>Mitigation Strategies:<br></b>{Mitigation_Strategies}</p>
      <p><b>Risk Owners:<br></b>{risk_owners_table}</p>
       <p><b>Initial Risk Register:</b>{risk_table}</p>
    <div style="border: 2px solid blue; padding: 10px; background-color: lightblue; display: inline-block; width: 8in;">
        <h3><b>Methodology and Tools</b></h3>
        </div><br>
        <p><b>Selected Project Management Methodology<br></b>{Selected_Project_Management_Methodology}</p>
        <p><b>Tools:<br></b>{Tools}</p>
        <p><b>Reporting Format and Frequency:<br></b>{Reporting_Format_and_Frequency}</p>
       <div style="border: 2px solid blue; padding: 10px; background-color: lightblue; display: inline-block; width: 8in;">
        <h3><b>Approval and Governance</b></h3>
        </div><br>
        <p><b>Project Charter Approval<br></b>{Project_Charter_Approval}</p>
        <p><b>Executive Sponsor Sign Off<br></b>{Executive_Sponsor_Sign_Off}</p>
        <p><b>Governance Model<br></b>{Governance_Model}</p>


    """

    display(HTML(html_content))



# Display project overview with stakeholder table
display_project_overview(path of charter)
