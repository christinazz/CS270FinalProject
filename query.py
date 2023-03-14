"""
CS270 Winter Quarter 2023 - Final Project
Contributers: Christina Sze, Maxwell Kounga, Rhea Mitr, Gabrielle Belanger

This file contains the code to interact with our Protege OWL file
and query the ontology to find relevant internships for students
interested in the biomedical and healthcare space.
"""

# import relevant packages
import owlready2
from owlready2 import *
import numpy as np

class Query:
    def __init__(self):
        # Initialize global query states
        self.company_types = None
        self.consulting_subtypes = None
        self.pharma_subtypes = None
        self.biotech_subtypes = None
        self.specialization = None
        self.size = None
        self.location = None

    def greeting(self):
        return "Hi! I'm a query search engine here to help you find relevant companies in the biotech and healthcare space. I'll prompt you for some information, and then return some results based on what you enter."

    def goodbye(self):
        return "Hope you found your results helpful. Feel free to rerun the program with a new query."
    
    def internship_query(self):
        """
        Allows users to query for internships given the possible query parameters (taken from global state):
        - company_type (list of str): 'consulting', 'pharma', or 'biotech'
        - subtype (list str): subtype of type of company (e.g. 'biotech' has subclasses 'therapeutics', 'diagnostic and analytical')
        - specialization (list of str): e.g. 'healthcare', 'drug discovery', etc.
        - size (int): size of company approximated by # of employees
        - location (list of str): location of company, should be in format 'City, State/Country'

        Returns a list of strs containing the company names, e.g. ['Bain&Company', 'Amgen', 'Regeneron'].
        """
        # import ontology (@Max, when you test, copy and paste the first line below and comment out the line with my file path)
        # you'll have to replace with the file path to your local copy of the ontology, starting it with file://
        onto = get_ontology("file:///Users/christinasze/Desktop/CS270/CS270FinalProject/BMI210-FinalProject-Ontology.owl").load()
        query_results = []  # for storing all results of query
        
        # Query contains a specified company type
        if self.company_types:
            if 'consulting' in self.company_types:
                consulting_class = onto.search(iri = "*Consulting_Firm*")
                consulting_results = onto.search(type = consulting_class[0], offersInternships = True)
                consulting_results = list(consulting_results)
                query_results = query_results + consulting_results
            
            if 'pharma' in self.company_types:
                pharma_class = onto.search(iri = "*Pharmaceutical_Company*")
                pharma_results = onto.search(type = pharma_class[0], offersInternships = True)
                pharma_results = list(pharma_results)
                query_results = query_results + pharma_results
            
            if 'biotech' in self.company_types:
                biotech_class = onto.search(iri = "*Biotech_Company*")
                biotech_results = onto.search(type = biotech_class[0], offersInternships = True)
                biotech_results = list(biotech_results)
                query_results = query_results + biotech_results
        else:
            pass

        return query_results
    
    def general_query(self):
        """
        Allows users to query companies given the possible query parameters (taken from global state):
        - company_type (list of str): 'consulting', 'pharma', or 'biotech'
        - subtype (list of str): subtype of type of company (e.g. 'biotech' has subclasses 'therapeutics', 'diagnostic and analytical')
        - specialization (list of str): e.g. 'healthcare', 'drug discovery', etc.
        - size (int): size of company approximated by # of employees
        - location (list of str): location of company, should be in format 'City, State/Country'

        Returns a list of strs containing the company names, e.g. ['Bain&Company', 'Amgen', 'Regeneron'].
        """
        # import ontology
        onto = get_ontology("file:///Users/christinasze/Desktop/CS270/CS270FinalProject/BMI210-FinalProject-Ontology.owl").load()
        print(list(onto.classes()))

        query_results = []  # for storing all results of query
        
        # Query contains a specified company type
        if self.company_types:
            if 'consulting' in self.company_types:
                consulting_class = onto.search(iri = "*Consulting_Firm*")
                consulting_results = onto.search(type = consulting_class[0])
                consulting_results = list(consulting_results)
                query_results = query_results + consulting_results
            
            if 'pharma' in self.company_types:
                pharma_class = onto.search(iri = "*Pharmaceutical_Company*")
                pharma_results = onto.search(type = pharma_class[0])
                pharma_results = list(pharma_results)
                query_results = query_results + pharma_results
            
            if 'biotech' in self.company_types:
                biotech_class = onto.search(iri = "*Biotech_Company*")
                biotech_results = onto.search(type = biotech_class[0])
                biotech_results = list(biotech_results)
                query_results = query_results + biotech_results
        else:
            pass

        return query_results

# Main Function
if __name__ == '__main__':
    query = Query()
    print(query.greeting())
    purpose = input("\nAre you looking for internships (type 'internship'), or are you just searching for a specific subset of companies in the biotech and healthcare space (type 'general')?  ")

    while purpose not in ['internship', 'general']:
        purpose = input("\nSorry, I didn't understand. Can you specify if you're looking for an internship (type 'internship') or doing a general query (type 'general')?  ")

    company_types = input("\nOkay, thanks! Do you want to specify a specific type of company you want to filter your query results by ('consulting', 'pharma', and/or 'biotech')? Separate each query input with commas. Otherwise, hit return. ")

    # User specified type(s) of companies to filter by
    if len(company_types) > 0: 
        company_types = company_types.split(',')
        types_list = []

        for t in company_types:
            if t.strip() in ['consulting', 'pharma', 'biotech']:
                types_list.append(t.strip())
            else:
                print(t, 'is not a valid company type. It will not be included in the query.')

        query.company_types = types_list
    
        # Given specified type(s), user can specify subtypes (user should not specify subtypes if no general types)
        if 'consulting' in types_list:
            print("\nWould you like to specify any subtypes of consulting firms?\n")
            consulting_subtypes = input("Type 'general' for general consulting firms and/or 'specialized' for consulting firms that specify in healthcare and biotech. Separate each query input with commas. Otherwise, hit return. ")
            
            # User specified subtype(s) of consulting firms to filter by
            if len(consulting_subtypes) > 0:
                consulting_subtypes = consulting_subtypes.split(',')
                consulting_subtypes_list = []

                for t in consulting_subtypes:
                    if t.strip() in ['general', 'specialized']:
                        consulting_subtypes_list.append(t.strip())
                    else:
                        print(t, 'is not a valid consulting subtype. It will not be included in the query.')
            
                query.consulting_subtypes = consulting_subtypes_list
        
        if 'pharma' in types_list:
            print("\nWould you like to specify any subtypes of pharmaceutical companies?\n")
            pharma_subtypes = input("Type 'generic', 'mainline', and/or 'research and development'. Separate each query input with commas. Otherwise, hit return. ")
            
            # User specified subtype(s) of consulting firms to filter by
            if len(pharma_subtypes) > 0:
                pharma_subtypes = pharma_subtypes.split(',')
                pharma_subtypes_list = []

                for t in pharma_subtypes:
                    if t.strip() in ['generic', 'mainline', 'research and development']:
                        pharma_subtypes_list.append(t.strip())
                    else:
                        print(t, 'is not a valid pharmaceutical subtype. It will not be included in the query.')
            
                query.pharma_subtypes = pharma_subtypes_list

        # Given specified type(s), user can specify subtypes (user should not specify subtypes if no general types)
        if 'biotech' in types_list:
            print("\nWould you like to specify any subtypes of biotech companies?\n")
            biotech_subtypes = input("Type 'diagnostics and analytical', 'digital health', 'drug delivery', 'genomics and proteomics', 'medical devices', 'therapeutics', and/or 'vetinary'. Separate each query input with commas. Otherwise, hit return. ")
            
            # User specified subtype(s) of consulting firms to filter by
            if len(biotech_subtypes) > 0:
                biotech_subtypes = biotech_subtypes.split(',')
                biotech_subtypes_list = []

                for t in biotech_subtypes:
                    if t.strip() in ['diagnostics and analytical', 'digital health', 'drug delivery', 'genomics and proteomics', 'medical devices', 'therapeutics', 'vetinary']:
                        biotech_subtypes_list.append(t.strip())
                    else:
                        print(t, 'is not a valid biotech subtype. It will not be included in the query.')
            
                query.biotech_subtypes = biotech_subtypes_list
            
    query_results = []
    if purpose == 'internship':
        query_results = query.internship_query()
    else:  # purpose == 'general'
        query_results = query.general_query()
    
    print('\nThe following companies matched your query:\n')

    for q in query_results:
        q_str = str(q)
        print(q_str[24:], '\n')

    print(query.goodbye())