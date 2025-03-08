# Example Usage

from scrape import *
from enums import SubjectCode 
from pprint import pprint

# To get all the Subject Codes and their full respective names
# The function below ruturns a list of tuples

subject_codes = getAllSubjectCodes()
pprint(subject_codes)

