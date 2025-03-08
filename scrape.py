import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from enums import SubjectCode 


def getAllSubjectCodes():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded', 
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }

    url = 'https://catalogue.uottawa.ca/en/courses/'

    response = requests.get(url, headers = headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    course_codes = []
    for course in soup.find_all('li')[:-1]:
        
        pattern = r'\(([A-Z]{3})\)'
        m = re.search(pattern, str(course.text))

        if m:
            course_codes.append((m.group(1), course.text.rsplit(' ', 1)[0]))

    return course_codes

def getCourseCatalogue(subject_code_ = SubjectCode.CSI):
    if not isinstance(subject_code_, SubjectCode):
        raise TypeError(f"Expected a SubjectCode enum, but got {type(subject_code_).__name__}")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded', 
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }

    url = f'https://catalogue.uottawa.ca/en/courses/{subject_code_.value}/'

    response = requests.get(url, headers = headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    course_selection = []
    for course in soup.find_all(class_ = 'courseblock'):
        name = course.find('strong').text
        highlight = course.find(class_ = 'highlight')
        prerequisites = None

        if highlight:
            prerequisites = highlight.text
            if ':' in prerequisites:
                prerequisites = prerequisites.split(':', 1)[1].replace('.', '').strip()

        
        subject_code_and_number, rest = name.split(' ', 1) # my bad for the long var name
        subject_code, course_number= subject_code_and_number.split('\xa0', 1)

        try:
            name, units = rest.split('(', 1)
        except ValueError:
            name = rest
            units = None
        
        name = name.strip()
        
        if units:
            units = units.replace(')', '')
            units = units.strip()
            pattern = r'[0-9]'
            m = re.match(pattern, units)

            if m:
                units = m.group(0)
            else:
                units = None 

        course_selection.append(
            {
                'subject_code': subject_code,
                'course_number': course_number,
                'name': name,
                'prerequisites': prerequisites,
                'units': units
            }
        )

    return pd.DataFrame(course_selection)

if __name__ == "__main__":
    print(getAllSubjectCodes())