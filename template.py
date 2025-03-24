#This file contains the templates of various charters (As of now, there is only one template)
#The variables found here are dictionaries. The sections are the keys and subsections are the values.
from variables import charter_input

template = {'Project Overview': ['Project Name', 'Project Start/End (projected)', 'Authorization Date'],
            'Business Case and Project Objectives': ['Problem Statement', 'Goals and Objectives', 'Expected Benefits', 'Strategic Alignment'],
            'Stakeholder Information': ['Stakeholder Register', 'Roles and Responsibilities', 'Communication Preferences'],
            'Project Scope': ['Scope Statement', 'Deliverables', 'Boundaries and Constraints'],
            'Requirements Documentation': ['Functional and Non-functional Requirements', 'Feature Description', 'Use Cases', 'User Stories', 'Input & Output Requirements', 'Performance Requirements', 'Security Requirements', 'Scalability', 'Compliance Requirements', 'Risk Considerations'],
            'Resources': ['Human Resources', 'Physical Resources', 'Budgetary Information'],
            'Timeline and Deadlines': ['High-Level Project Schedule', 'Key Dates and Deliverables', 'Dependencies and Critical Path'],
            'Risk Assessment': ['Initial Risk Register', 'Mitigation Strategies', 'Risk Owners'],
            'Methodology and Tools': ['Selected Project Management Methodology', 'Tools', 'Reporting Format and Frequency'],
            'Approval and Governance': ['Project Charter Approval', 'Executive Sponsor Sign-Off', 'Governance Model']
            }

template_for_frd = {
       'Introduction': ['Project Name', 'Document Purpose', 'Scope Statement', 'Boundaries and Constraints'],
       'Overview': ['Background', 'Goals and Objectives', 'Strategic Alignment'],
       'Functional Requirements': ['Feature Description', 'Use Cases', 'User Stories', 'Input & Output Requirements'],
       'Non Functional Requirements': ['Performance Requirements', 'Security Requirements', 'Scalability', 'Compliance Requirements'],
       'Risks & Mitigations': ['Initial Risk Register', 'Risks & Mitigations'],
       'Dependencies': ['Dependencies and Critical Path'],
       }

template_for_charter = {
'Project Overview': ['Project Name', 'Project Start(projected)', 'Project End(projected)', 'Authorization Date'],
            'Business Case and Project Objectives': ['Problem Statement', 'Goals and Objectives', 'Expected Benefits', 'Strategic Alignment'],
            'Stakeholder Information': ['Stakeholder Register', 'Roles and Responsibilities', 'Communication Preferences'],
            'Project Scope': ['Scope Statement', 'Deliverables', 'Boundaries and Constraints'],
            'Requirements Documentation': ['Functional Requirements', 'Non-functional Requirements', 'Compliance Requirements', 'Risk Considerations'],
            'Resources': ['Human Resources', 'Physical Resources', 'Budgetary Information'],
            'Timeline and Deadlines': ['High-Level Project Schedule', 'Key Dates', 'Deliverables', 'Dependencies and Critical Path'],
            'Risk Assessment': ['Initial Risk Register', 'Mitigation Strategies', 'Risk Owners'],
            'Methodology and Tools': ['Selected Project Management Methodology', 'Tools', 'Reporting Format and Frequency'],
            'Approval and Governance': ['Project Charter Approval', 'Executive Sponsor Sign-Off', 'Governance Model']
}

template_for_brd = {'executive summary':['executive summary']}