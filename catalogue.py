# Example usage

from scrape import *
from enums import SubjectCode
import pandas as pd

# Say you want to get all the CEG courses
courses = getCourseCatalogue(SubjectCode.CEG) 

# Note: if you want to see all the available subject code, take a look at enums.py 

# The function returns a pd.DataFrame

# Remove the rows and columns limit when printing to the standard output
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(courses[['course_number', 'name', 'units', 'prerequisites']])