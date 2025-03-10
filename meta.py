# The list below was obtained using the getAllSubjectCodes function in scrape.py
# You don't really need this file
# This script was used to generate enums.py

s = \
'''
Accounting (CPT)
Administration (ADM)
Advanced Materials and Manufacturing (AMM)
African Studies (AFR)
Anatomical Sciences Education (ASE)
Anatomy and Neurobiology (ANA)
Anatomy and Physiology (ANP)
Anesthesiology (ANE)
Anthropology (ANT)
Arabic Language and Culture (ARB)
Arts Co-op (ACP)
Arts, Music, Theatre (AMT)
Asian Studies (ASI)
Bilingualism Studies (BIL)
Biochemistry (BCH)
Bioinformatics (BNF)
Biology (BIO)
Biomedical Engineering (BMG)
Biomedical Science (BIM)
Biomolecular Sciences (BML)
Biopharmaceutical Science (BPS)
Canadian Studies (CDN)
Cardio-Respiratory Systems (CTS)
Cellular and Molecular Medicine (CMM)
Celtic Studies (CLT)
Chemical and Environmental Toxicology (TOX)
Chemical Engineering (CHG)
Chemistry (CHM)
Chinese (CHN)
Civil Engineering (CVG)
Civil Law (DRC)
Classical Studies (CLA)
Classics (LCL)
Clinical Rotation (CLI)
Common Law (CML)
Communication (CMN)
Complex Project Leadership (CPL)
Computer Engineering (CEG)
Computer Science (CSI)
Conflict Studies and Human Rights (ECH)
Criminology (CRM)
Cybersecurity (SEC)
Data Science (SDS)
Digital Cultures (DCN) 
Digital Humanities (DHN)
Digital Transformation and Innovation (DTI)
Doctoral Thesis (THD)
Economics (ECO)
Education (EDU)
Education (PED)
Elective Courses in Medicine (ELE)
Electrical Engineering (ELG)
Engineering Co-op (CGI)
Engineering Design and Teaching Innovation (SED)
Engineering Management (EMP)
English (ENG)
English as a Second Language (ESL)
Entrepreneurial Engineering Design (EED)
Environmental Engineering (EVG)
Environmental Science (EVS)
Environmental Studies (ENV)
Environmental Sustainability (EVD)
Epidemiology and Public Health (EPI)
Family Medicine (FAM)
Feminist and Gender Studies (FEM)
Film Studies (CIN)
Food and Nutrition (NUT)
Francophone Studies (EFR)
French as a Second Language (FLS)
French Studies (FRE)
Gastroenteritis (GAE)
General Engineering (GNG)
General Surgery (GSU)
Geography (GEG)
Geology (GEO)
German Language and Culture (ALG)
Gerontology (GRT)
Health Administration (HAH)
Health Administration (MHA)
Health Sciences (HSS)
Health Systems (MHS)
History (HIS)
Human and Molecular Genetics (HMG)
Human Kinetics (APA)
Immunology (IMM)
Indigenous Languages (ILA)
Indigenous Studies (EAS)
Information Studies (ISI)
Information Technology (ITI)
Interdisciplinary Artificial Intelligence (IAI)
Interdisciplinary Study in Arts (AHL)
International Development and Globalization (DVM)
Interprofessional Health Care Practice (SAI)
Italian Language and Culture (ITA)
Japanese (JPN)
Journalism (JOU)
Latin American Studies (ELA)
Law (Certificate) (DCC)
Law (DCL)
Leisure Studies (LSR)
Lettres françaises (FRA)
Linguistics (LIN)
Major Research Paper (MRP)
Management (MGT)
Master's Thesis (THM)
Mathematics (MAT)
MBA Program (MBA)
Mechanical Engineering (MCG)
Medical Intern or Resident (INR)
Medicine (MED)
Medicine (PCS)
Medieval Studies (MDV)
Microbiology and Immunology (MIC)
Modern Languages (LLM)
Music (MUS)
Neurology (NAP)
Neuroscience (NSC)
Notary Law (NOT)
Nursing (NSG)
Obstetrics and Gynecology (OBG)
Occupational Therapy (ERG)
Ophthalmic Medical Technology (OMT)
Ophthalmology (OPH)
Orthopaedic Pathology (ORT)
Pathology and Experimental Medicine (PME)
Pediatrics (PAE)
Pharmacology (PHA)
Philosophy (PHI)
Physics (PHY)
Physiology (PHS)
Physiotherapy (PHT)
Polish (PLN)
Political Science (POL)
Population Health (POP)
Population Health Risk Assessment and Management (PHR)
Portuguese (POR)
Pre-internship Program (PIP)
Psychiatry (PCT)
Psychology (PSY)
Public Administration (PAP)
Public and International Affairs (API)
Radiology (RAD)
Rehabilitation Sciences (REA)
Religious Studies (SRS)
Research Internship (RCH)
Russian Language and Culture (RUS)
Science (General) (SCI)
Science, Society and Policy (ISP)
Second-Language Teaching (DLS)
Social Sciences (FSS)
Social Sciences (SCS)
Social Sciences of Health (SSS)
Social Work (TSO)
Sociology (SOC)
Software Engineering (SEG)
Spanish (ESP)
Speech-Language Pathology (ORA)
Systems Science (SYS)
Theatre (THE)
Translation (TRA)
Translational and Molecular Medicine (TMM)
uOGlobal (GLO)
Urology (URO)
Vered Jewish Canadian Studies (JCS)
Visual Arts (ART) 
World Literatures and Cultures (LCM)
Yiddish (YDD)
'''
import re

lines = []
for e in s.split('\n'):
    if e:
        pattern = r'\([A-Z]+\)'
        m = re.search(pattern , e)
        code = m.group(0).translate(str.maketrans({')': None, '(': None}))

        name = e.split('(', 1)[0].strip()
        if m:
            line = f'{code} = "{code.lower()}"\t # {name}'
            lines.append((4 * ' ') + line)


pre = [
    'from enum import Enum, auto',
    '\n'
    'class SubjectCode(Enum): '
]


with open('enums.py', 'w') as f:
    f.writelines([l + '\n' for l in pre + lines])

