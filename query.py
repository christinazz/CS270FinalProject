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

def common(query1, query2):
    result_list = []
    for q in query1:
        if q in query2:
            result_list = result_list + [q]
    return result_list

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
        self.revenue = None
        self.public = None

    def greeting(self):
        return "Hi! I'm a query search engine here to help you find relevant companies in the biotech and healthcare space. I'll prompt you for some information, and then return some results based on what you enter.\n"

    def goodbye(self):
        return "Hope you found your results helpful. Feel free to rerun the program with a new query.\n"

    def internship_query(self):
        """
        Allows users to query for internships given the possible query parameters (taken from global state):
        - subtype (list str): subtype of type of company (e.g. 'biotech' has subclasses 'therapeutics', 'diagnostic and analytical')
        Returns a list of strs containing the company names, e.g. ['Bain&Company', 'Amgen', 'Regeneron'].
        """
        # Max's path: /Users/maxkounga/Desktop/School/StanfordY3/Winter Q3/CS 270/Project/
        onto = get_ontology("file:///Users/christinasze/Desktop/CS270/CS270FinalProject/BMI210-FinalProject-Ontology.owl").load()
        query_results = []  # for storing all results of query

        # Query contains a specified company type
        if self.company_types:
            if 'consulting' in self.company_types:
                if self.consulting_subtypes:
                    if 'general' in self.consulting_subtypes:
                        gen_consulting_class = onto.search(iri="*General_Consulting*")
                        gen_consulting_results = onto.search(type=gen_consulting_class[0], offersInternships=True)
                        gen_consulting_results = list(gen_consulting_results)
                        query_results = query_results + gen_consulting_results
                        
                    if 'specialized' in self.consulting_subtypes:
                        spec_consulting_class = onto.search(iri="*Specialized_Consulting*")
                        spec_consulting_results = onto.search(type=spec_consulting_class[0], offersInternships=True)
                        spec_consulting_results = list(spec_consulting_results)
                        query_results = query_results + spec_consulting_results
                else:
                    consulting_class = onto.search(iri="*Consulting_Firm*")
                    consulting_results = onto.search(type=consulting_class[0], offersInternships=True)
                    consulting_results = list(consulting_results)
                    query_results = query_results + consulting_results

            if 'pharma' in self.company_types:
                if self.pharma_subtypes:
                    if 'generic' in self.pharma_subtypes:
                        generic_class = onto.search(iri="*Generic*")
                        generic_results = onto.search(type=generic_class[0], offersInternships=True)
                        generic_results = list(generic_results)
                        query_results = query_results + generic_results
                        
                    if 'mainline' in self.pharma_subtypes:
                        mainline_class = onto.search(iri="*Mainline*")
                        mainline_results = onto.search(type=mainline_class[0], offersInternships=True)
                        mainline_results = list(mainline_results)
                        query_results = query_results + mainline_results
                        
                    if 'research and development' in self.pharma_subtypes:
                        rd_class = onto.search(iri="*Research_and_Development*")
                        rd_results = onto.search(type=rd_class[0], offersInternships=True)
                        rd_results = list(rd_results)
                        query_results = query_results + rd_results
                else:
                    pharma_class = onto.search(iri="*Pharmaceutical_Company*")
                    pharma_results = onto.search(type=pharma_class[0], offersInternships=True)
                    pharma_results = list(pharma_results)
                    query_results = query_results + pharma_results

            if 'biotech' in self.company_types:
                if self.biotech_subtypes:
                    if 'diagnostics and analytical' in self.biotech_subtypes:
                        daa_class = onto.search(iri="*Diagnostics_and_Analytical*")
                        daa_results = onto.search(type=daa_class[0], offersInternships=True)
                        daa_results = list(daa_results)
                        query_results = query_results + daa_results
                        
                    if 'digital health' in self.biotech_subtypes:
                        dh_class = onto.search(iri="*Digital_Health*")
                        dh_results = onto.search(type=dh_class[0], offersInternships=True)
                        dh_results = list(dh_results)
                        query_results = query_results + dh_results

                    if 'genomics and proteomics' in self.biotech_subtypes:
                        gap_class = onto.search(iri="*Genomics_and_Proteomics*")
                        gap_results = onto.search(type=gap_class[0], offersInternships=True)
                        gap_results = list(gap_results)
                        query_results = query_results + gap_results
                        
                    if 'medical devices' in self.biotech_subtypes:
                        med_class = onto.search(iri="*Medical_Devices*")
                        med_results = onto.search(type=med_class[0], offersInternships=True)
                        med_results = list(med_results)
                        query_results = query_results + med_results
                        
                    if 'therapeutics' in self.biotech_subtypes:
                        therp_class = onto.search(iri="*Therapeutics*")
                        therp_results = onto.search(type=therp_class[0], offersInternships=True)
                        therp_results = list(therp_results)
                        query_results = query_results + therp_results
                        
                    if 'vetinary' in self.biotech_subtypes:
                        vet_class = onto.search(iri="*Vetinary*")
                        vet_results = onto.search(type=vet_class[0], offersInternships=True)
                        vet_results = list(vet_results)
                        query_results = query_results + vet_results
                    
                    if 'drug delivery' in self.biotech_subtypes:
                        dd_class = onto.search(iri="*Drug_Delivery*")
                        dd_results = onto.search(type=dd_class[0], offersInternships=True)
                        dd_results = list(dd_results)
                        query_results = query_results + dd_results
                else:
                    biotech_class = onto.search(iri="*Biotech_Company*")
                    biotech_results = onto.search(type=biotech_class[0], offersInternships=True)
                    biotech_results = list(biotech_results)
                    query_results = query_results + biotech_results
        else:
            query_results = list(onto.individuals())

        return query_results

    def general_query(self):
        """
        Allows users to query companies given the possible query parameters (taken from global state):
        - subtype (list of str): subtype of type of company (e.g. 'biotech' has subclasses 'therapeutics', 'diagnostic and analytical')
        Returns a list of strs containing the company names, e.g. ['Bain&Company', 'Amgen', 'Regeneron'].
        """
        # import ontology
        # onto = get_ontology("/Users/maxkounga/Desktop/School/StanfordY3/Winter Q3/CS 270/Project/BMI210-FinalProject-Ontology.owl").load()
        onto = get_ontology("file:///Users/christinasze/Desktop/CS270/CS270FinalProject/BMI210-FinalProject-Ontology.owl").load()

        query_results = []  # for storing all results of query

        # Query contains a specified company type
        if self.company_types:
            if 'consulting' in self.company_types:
                if self.consulting_subtypes:
                    if 'general' in self.consulting_subtypes:
                        gen_consulting_class = onto.search(iri="*General_Consulting*")
                        gen_consulting_results = onto.search(type=gen_consulting_class[0])
                        gen_consulting_results = list(gen_consulting_results)
                        query_results = query_results + gen_consulting_results
                        
                    if 'specialized' in self.consulting_subtypes:
                        spec_consulting_class = onto.search(iri="*Specialized_Consulting*")
                        spec_consulting_results = onto.search(type=spec_consulting_class[0])
                        spec_consulting_results = list(spec_consulting_results)
                        query_results = query_results + spec_consulting_results
                else:
                    consulting_class = onto.search(iri="*Consulting_Firm*")
                    consulting_results = onto.search(type=consulting_class[0])
                    consulting_results = list(consulting_results)
                    query_results = query_results + consulting_results

            if 'pharma' in self.company_types:
                if self.pharma_subtypes:
                    if 'generic' in self.pharma_subtypes:
                        generic_class = onto.search(iri="*Generic*")
                        generic_results = onto.search(type=generic_class[0])
                        generic_results = list(generic_results)
                        query_results = query_results + generic_results
                        
                    if 'mainline' in self.pharma_subtypes:
                        mainline_class = onto.search(iri="*Mainline*")
                        mainline_results = onto.search(type=mainline_class[0])
                        mainline_results = list(mainline_results)
                        query_results = query_results + mainline_results
                        
                    if 'research and development' in self.pharma_subtypes:
                        rd_class = onto.search(iri="*Research_and_Development*")
                        rd_results = onto.search(type=rd_class[0])
                        rd_results = list(rd_results)
                        query_results = query_results + rd_results
                else:
                    pharma_class = onto.search(iri="*Pharmaceutical_Company*")
                    pharma_results = onto.search(type=pharma_class[0])
                    pharma_results = list(pharma_results)
                    query_results = query_results + pharma_results

            if 'biotech' in self.company_types:
                if self.biotech_subtypes:
                    if 'diagnostics and analytical' in self.biotech_subtypes:
                        daa_class = onto.search(iri="*Diagnostics_and_Analytical*")
                        daa_results = onto.search(type=daa_class[0])
                        daa_results = list(daa_results)
                        query_results = query_results + daa_results
                        
                    if 'digital health' in self.biotech_subtypes:
                        dh_class = onto.search(iri="*Digital_Health*")
                        dh_results = onto.search(type=dh_class[0])
                        dh_results = list(dh_results)
                        query_results = query_results + dh_results

                    if 'genomics and proteomics' in self.biotech_subtypes:
                        gap_class = onto.search(iri="*Genomics_and_Proteomics*")
                        gap_results = onto.search(type=gap_class[0])
                        gap_results = list(gap_results)
                        query_results = query_results + gap_results
                        
                    if 'medical devices' in self.biotech_subtypes:
                        med_class = onto.search(iri="*Medical_Devices*")
                        med_results = onto.search(type=med_class[0])
                        med_results = list(med_results)
                        query_results = query_results + med_results
                        
                    if 'therapeutics' in self.biotech_subtypes:
                        therp_class = onto.search(iri="*Therapeutics*")
                        therp_results = onto.search(type=therp_class[0])
                        therp_results = list(therp_results)
                        query_results = query_results + therp_results
                        
                    if 'vetinary' in self.biotech_subtypes:
                        vet_class = onto.search(iri="*Vetinary*")
                        vet_results = onto.search(type=vet_class[0])
                        vet_results = list(vet_results)
                        query_results = query_results + vet_results

                    if 'drug delivery' in self.biotech_subtypes:
                        dd_class = onto.search(iri="*Drug_Delivery*")
                        dd_results = onto.search(type=dd_class[0])
                        dd_results = list(dd_results)
                        query_results = query_results + dd_results
                else:
                    biotech_class = onto.search(iri="*Biotech_Company*")
                    biotech_results = onto.search(type=biotech_class[0])
                    biotech_results = list(biotech_results)
                    query_results = query_results + biotech_results
        else:
            query_results = list(onto.individuals())

        return query_results

    def purpose_query(self):
        """
        Allows users to query for internships given the possible query parameters (taken from global state):
        - company_type (list of str): 'consulting', 'pharma', or 'biotech'
        - subtype (list str): subtype of type of company (e.g. 'biotech' has subclasses 'therapeutics', 'diagnostic and analytical')
        Returns a list of strs containing the company names, e.g. ['Bain&Company', 'Amgen', 'Regeneron'].
        """
        # import ontology (@Max, when you test, copy and paste the first line below and comment out the line with my file path)
        # you'll have to replace with the file path to your local copy of the ontology, starting it with file://
        # onto = get_ontology("/Users/maxkounga/Desktop/School/StanfordY3/Winter Q3/CS 270/Project/BMI210-FinalProject-Ontology.owl").load()
        onto = get_ontology("file:///Users/christinasze/Desktop/CS270/CS270FinalProject/BMI210-FinalProject-Ontology.owl").load()
        query_results = []  # for storing all results of query

        purpose = input(
            "\nAre you looking for internships (type 'internship'), or are you just searching for a specific subset of companies in the biotech and healthcare space (type 'general')?\n")

        while purpose not in ['internship', 'general']:
            purpose = input(
                "\nSorry, I didn't understand. Can you specify if you're looking for an internship (type 'internship') or doing a general query (type 'general')?\n")

        company_types = input(
            "\nOkay, thanks! Do you want to specify a specific type of company you want to filter your query results by ('consulting', 'pharma', and/or 'biotech')? Separate each query input with commas. Otherwise, hit return.\n")

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
                consulting_subtypes = input(
                    "Type 'general' for general consulting firms and/or 'specialized' for consulting firms that specify in healthcare and biotech. Separate each query input with commas. Otherwise, hit return. ")

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
                pharma_subtypes = input(
                    "Type 'generic', 'mainline', and/or 'research and development'. Separate each query input with commas. Otherwise, hit return. ")

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
                biotech_subtypes = input(
                    "Type 'diagnostics and analytical', 'digital health', 'drug delivery', 'genomics and proteomics', 'medical devices', 'therapeutics', and/or 'vetinary'. Separate each query input with commas. Otherwise, hit return. ")

                # User specified subtype(s) of consulting firms to filter by
                if len(biotech_subtypes) > 0:
                    biotech_subtypes = biotech_subtypes.split(',')
                    biotech_subtypes_list = []

                    for t in biotech_subtypes:
                        if t.strip() in ['diagnostics and analytical', 'digital health', 'drug delivery',
                                         'genomics and proteomics', 'medical devices', 'therapeutics', 'vetinary']:
                            biotech_subtypes_list.append(t.strip())
                        else:
                            print(t, 'is not a valid biotech subtype. It will not be included in the query.')

                    query.biotech_subtypes = biotech_subtypes_list

        if purpose == 'internship':
            query_results = query.internship_query()
        else:  # purpose == 'general'
            query_results = query.general_query()

        return query_results

    def location_query(self):
        """
        Allows users to query for internships given the possible query parameters (taken from global state):
        - location (list of str): location of company, should be in format 'City, State/Country'
        Returns a list of strs containing the company names, e.g. ['Bain&Company', 'Amgen', 'Regeneron'].
        """
        # import ontology (@Max, when you test, copy and paste the first line below and comment out the line with my file path)
        # you'll have to replace with the file path to your local copy of the ontology, starting it with file://
        # onto = get_ontology("/Users/maxkounga/Desktop/School/StanfordY3/Winter Q3/CS 270/Project/BMI210-FinalProject-Ontology.owl").load()
        onto = get_ontology("file:///Users/christinasze/Desktop/CS270/CS270FinalProject/BMI210-FinalProject-Ontology.owl").load()
        query_results = []  # for storing all results of query

        location = input("\nWhich location are you interested in? Enter in the format 'City, State/Country\n")
        eligible_cities = ['New York, New York', 'London, England', 'Boston, Massachusetts', 'Dublin, Ireland',
                           'Evanston, Illnois', 'Chicago, Illinois', 'Melbourne, Australia', 'Paris, France',
                           'Wall Township, New Jersey', 'San Francisco, California', 'Waltham, Massachusetts',
                           'Centennial, Connecticut', 'Alameda, California', 'Kensington, California', 'Washington, D.C.',
                           'Durham, North Carolina','Foster City, California, United States','Thousand Oaks, California',
                           'Mount Pleasant, New York', 'Ontario, Canada', 'Burlington, North Carolina', 'Ravenswood, Illinois',
                           'Marcy-lÉtoile, France', 'Hilden, Germany', 'Hercules, California', 'San Diego, California',
                           'Cambridge, Massachusetts', 'Madison, Wisconsin', 'Salt Lake City, Utah', 'Berkeley, California',
                           'Somerville, Massachusetts', 'Zug, Switzerland', 'Los Angeles, California', 'Rahway, New Jersey',
                           'Westbrook, Maine', 'Portland, Maine', 'Parsippany, New Jersey', 'Franklin Lakes, New Jersey',
                           'Deerfield, Illinois', 'Erlangen, Germany', 'Eindhoven, Netherlands', 'Billerica, Massachussets',
                           'Madrid, Spain', 'Cincinnati, Ohio', 'Kansas City, Missouri', 'Westwood, Massachussets',
                           'Hyderabad, India', 'Cambridge, United Kingdom', 'Laval, Canada', 'Leverkusen, Germany',
                           'Lynn, Norfolk, United Kingdom', 'Mainz, Germany', 'Ingelheim am Rhein, Germany', 'Somerset, New Jersey',
                           'Kansas City, Missouri', 'Brampton, Ontario, Canada', 'Indianapolis, Indiana']

        while location not in eligible_cities:
            location = input(
                "\nSorry, there are no companies headquartered in this city, try a different city.")

        location_results = onto.search(Headquarters=location)
        location_results = list(location_results)
        query_results = query_results + location_results

        return query_results

    def revenue_query(self):
        """
        Allows users to query for internships given the possible query parameters (taken from global state):
        - revenue (int): the net revenue of the company.
        Returns a list of strs containing the company names, e.g. ['Bain&Company', 'Amgen', 'Regeneron'].
        """
        # import ontology (@Max, when you test, copy and paste the first line below and comment out the line with my file path)
        # you'll have to replace with the file path to your local copy of the ontology, starting it with file://
        # onto = get_ontology("/Users/maxkounga/Desktop/School/StanfordY3/Winter Q3/CS 270/Project/BMI210-FinalProject-Ontology.owl").load()
        onto = get_ontology("file:///Users/christinasze/Desktop/CS270/CS270FinalProject/BMI210-FinalProject-Ontology.owl").load()
        query_results = []  # for storing all results of query

        revenue_str = input("\nWhat is the minimum revenue of your company of interest?\n")
        revenue = int(revenue_str)

        for inst in list(onto.individuals()):
            if inst.hasRevenue != []:
                if inst.hasRevenue[0] >= revenue:
                    query_results = query_results + [inst]

        return query_results

    def public_query(self):
        """
        Allows users to query for internships given the possible query parameters (taken from global state):
        - public (str): whether they want to query through public companies or not
        Returns a list of strs containing the company names, e.g. ['Bain&Company', 'Amgen', 'Regeneron'].
        """
        # import ontology (@Max, when you test, copy and paste the first line below and comment out the line with my file path)
        # you'll have to replace with the file path to your local copy of the ontology, starting it with file://
        # onto = get_ontology("/Users/maxkounga/Desktop/School/StanfordY3/Winter Q3/CS 270/Project/BMI210-FinalProject-Ontology.owl").load()
        onto = get_ontology("file:///Users/christinasze/Desktop/CS270/CS270FinalProject/BMI210-FinalProject-Ontology.owl").load()
        query_results = []  # for storing all results of query

        public = input("\nWould you like to query public companies, yes or no?\n")

        while public not in ['yes', 'no']:
            public = input(
                "\nSorry, you must enter in yes or no.")

        if public == 'yes':
            public_results = onto.search(isPublic=True)
        else:
            public_results = onto.search(isPublic=False)
        public_results = list(public_results)
        query_results = query_results + public_results

        return query_results

    def size_query(self):
        """
        Allows users to query for internships given the possible query parameters (taken from global state):
        - size (int): size of company approximated by # of employees
        Returns a list of strs containing the company names, e.g. ['Bain&Company', 'Amgen', 'Regeneron'].
        """
        # import ontology (@Max, when you test, copy and paste the first line below and comment out the line with my file path)
        # you'll have to replace with the file path to your local copy of the ontology, starting it with file://
        # onto = get_ontology("/Users/maxkounga/Desktop/School/StanfordY3/Winter Q3/CS 270/Project/BMI210-FinalProject-Ontology.owl").load()
        onto = get_ontology("file:///Users/christinasze/Desktop/CS270/CS270FinalProject/BMI210-FinalProject-Ontology.owl").load()
        query_results = []  # for storing all results of query

        size_str = input("\nWhat is the maximum number of employees you would like the company to have?\n")
        size = int(size_str)

        for inst in list(onto.individuals()):
            if inst.hasSize != []:
                if inst.hasSize[0] <= size:
                    query_results = query_results + [inst]

        return query_results

# Main Function
if __name__ == '__main__':
    query = Query()
    print(query.greeting())

    filter_selection = input("\nOkay, thanks! What would you like to filter your query results by:\n1. 'search purpose'\n2. 'company location'\n3. 'company revenue'\n4. 'company public status'\n5. 'company size'\nSeparate each query filter with a comma. If all, hit return.\n")
    if len(filter_selection) > 0:
        filter_selection = filter_selection.split(',')
        filter_list = []

        for t in filter_selection:
            if t.strip() in ['search purpose', 'company location', 'company revenue', 'company public status', 'company size']:
                filter_list.append(t.strip())
            else:
                print(t, 'is not a valid company type. It will not be included in the query.')
    else:
        filter_list = ['search purpose', 'company location', 'company revenue', 'company public status', 'company size']

    keepGoing = 0
    old_list = []
    query_results = []

    for selection in filter_list:
        if selection == 'search purpose':
            query_results = query.purpose_query()
        if selection == 'company location':
            query_results = query.location_query()
        if selection == 'company revenue':
            query_results = query.revenue_query()
        if selection == 'company public status':
            query_results = query.public_query()
        if selection == 'company size':
            query_results = query.size_query()
        if keepGoing > 0:
            query_results = common(query_results, old_list)
        old_list = query_results
        keepGoing += 1

    print('\nThe following companies matched your query:\n')

    for q in query_results:
        q_str = str(q)
        if q_str.find('.') == -1:
            print('- ',q_str[24:], '\n')
        else:
            print('- ', q_str[q_str.find('.') + 1:],  '\n')

    print(query.goodbye())