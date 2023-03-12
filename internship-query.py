"""
CS270 Winter Quarter 2023 - Final Project
Contributers: Christina Sze, Maxwell Kounga

This file contains the code to interact with our Protege OWL file
and query the ontology to find relevant internships for students
interested in the biomedical and healthcare space.
"""

# import relevant packages

import owlready2
import numpy as np

def internship_query(company_type = None, subtype = None, specialization = None, size = None):
    """
    Allows users to query for internships given the possible query parameters:
    - company_type (str): 'consulting', 'pharma', or 'biotech'
    - subtype (str): subtype of type of company (e.g. 'biotech' has subclasses 'therapeutics', 'diagnostic and analytical')
    - specialization (str): e.g. 'healthcare', 'drug discovery', etc.
    - size (int): size of company approximated by # of employees
    - location (str): location of company, should be in format 'City, State/Country'
    """