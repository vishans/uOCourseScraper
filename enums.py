from enum import Enum, auto

class SubjectCode(Enum): 
    CPT = "cpt"	 # Accounting
    ADM = "adm"	 # Administration
    AMM = "amm"	 # Advanced Materials and Manufacturing
    AFR = "afr"	 # African Studies
    ASE = "ase"	 # Anatomical Sciences Education
    ANA = "ana"	 # Anatomy and Neurobiology
    ANP = "anp"	 # Anatomy and Physiology
    ANE = "ane"	 # Anesthesiology
    ANT = "ant"	 # Anthropology
    ARB = "arb"	 # Arabic Language and Culture
    ACP = "acp"	 # Arts Co-op
    AMT = "amt"	 # Arts, Music, Theatre
    ASI = "asi"	 # Asian Studies
    BIL = "bil"	 # Bilingualism Studies
    BCH = "bch"	 # Biochemistry
    BNF = "bnf"	 # Bioinformatics
    BIO = "bio"	 # Biology
    BMG = "bmg"	 # Biomedical Engineering
    BIM = "bim"	 # Biomedical Science
    BML = "bml"	 # Biomolecular Sciences
    BPS = "bps"	 # Biopharmaceutical Science
    CDN = "cdn"	 # Canadian Studies
    CTS = "cts"	 # Cardio-Respiratory Systems
    CMM = "cmm"	 # Cellular and Molecular Medicine
    CLT = "clt"	 # Celtic Studies
    TOX = "tox"	 # Chemical and Environmental Toxicology
    CHG = "chg"	 # Chemical Engineering
    CHM = "chm"	 # Chemistry
    CHN = "chn"	 # Chinese
    CVG = "cvg"	 # Civil Engineering
    DRC = "drc"	 # Civil Law
    CLA = "cla"	 # Classical Studies
    LCL = "lcl"	 # Classics
    CLI = "cli"	 # Clinical Rotation
    CML = "cml"	 # Common Law
    CMN = "cmn"	 # Communication
    CPL = "cpl"	 # Complex Project Leadership
    CEG = "ceg"	 # Computer Engineering
    CSI = "csi"	 # Computer Science
    ECH = "ech"	 # Conflict Studies and Human Rights
    CRM = "crm"	 # Criminology
    SEC = "sec"	 # Cybersecurity
    SDS = "sds"	 # Data Science
    DCN = "dcn"	 # Digital Cultures
    DHN = "dhn"	 # Digital Humanities
    DTI = "dti"	 # Digital Transformation and Innovation
    THD = "thd"	 # Doctoral Thesis
    ECO = "eco"	 # Economics
    EDU = "edu"	 # Education
    PED = "ped"	 # Education
    ELE = "ele"	 # Elective Courses in Medicine
    ELG = "elg"	 # Electrical Engineering
    CGI = "cgi"	 # Engineering Co-op
    SED = "sed"	 # Engineering Design and Teaching Innovation
    EMP = "emp"	 # Engineering Management
    ENG = "eng"	 # English
    ESL = "esl"	 # English as a Second Language
    EED = "eed"	 # Entrepreneurial Engineering Design
    EVG = "evg"	 # Environmental Engineering
    EVS = "evs"	 # Environmental Science
    ENV = "env"	 # Environmental Studies
    EVD = "evd"	 # Environmental Sustainability
    EPI = "epi"	 # Epidemiology and Public Health
    FAM = "fam"	 # Family Medicine
    FEM = "fem"	 # Feminist and Gender Studies
    CIN = "cin"	 # Film Studies
    NUT = "nut"	 # Food and Nutrition
    EFR = "efr"	 # Francophone Studies
    FLS = "fls"	 # French as a Second Language
    FRE = "fre"	 # French Studies
    GAE = "gae"	 # Gastroenteritis
    GNG = "gng"	 # General Engineering
    GSU = "gsu"	 # General Surgery
    GEG = "geg"	 # Geography
    GEO = "geo"	 # Geology
    ALG = "alg"	 # German Language and Culture
    GRT = "grt"	 # Gerontology
    HAH = "hah"	 # Health Administration
    MHA = "mha"	 # Health Administration
    HSS = "hss"	 # Health Sciences
    MHS = "mhs"	 # Health Systems
    HIS = "his"	 # History
    HMG = "hmg"	 # Human and Molecular Genetics
    APA = "apa"	 # Human Kinetics
    IMM = "imm"	 # Immunology
    ILA = "ila"	 # Indigenous Languages
    EAS = "eas"	 # Indigenous Studies
    ISI = "isi"	 # Information Studies
    ITI = "iti"	 # Information Technology
    IAI = "iai"	 # Interdisciplinary Artificial Intelligence
    AHL = "ahl"	 # Interdisciplinary Study in Arts
    DVM = "dvm"	 # International Development and Globalization
    SAI = "sai"	 # Interprofessional Health Care Practice
    ITA = "ita"	 # Italian Language and Culture
    JPN = "jpn"	 # Japanese
    JOU = "jou"	 # Journalism
    ELA = "ela"	 # Latin American Studies
    DCC = "dcc"	 # Law
    DCL = "dcl"	 # Law
    LSR = "lsr"	 # Leisure Studies
    FRA = "fra"	 # Lettres françaises
    LIN = "lin"	 # Linguistics
    MRP = "mrp"	 # Major Research Paper
    MGT = "mgt"	 # Management
    THM = "thm"	 # Master's Thesis
    MAT = "mat"	 # Mathematics
    MBA = "mba"	 # MBA Program
    MCG = "mcg"	 # Mechanical Engineering
    INR = "inr"	 # Medical Intern or Resident
    MED = "med"	 # Medicine
    PCS = "pcs"	 # Medicine
    MDV = "mdv"	 # Medieval Studies
    MIC = "mic"	 # Microbiology and Immunology
    LLM = "llm"	 # Modern Languages
    MUS = "mus"	 # Music
    NAP = "nap"	 # Neurology
    NSC = "nsc"	 # Neuroscience
    NOT = "not"	 # Notary Law
    NSG = "nsg"	 # Nursing
    OBG = "obg"	 # Obstetrics and Gynecology
    ERG = "erg"	 # Occupational Therapy
    OMT = "omt"	 # Ophthalmic Medical Technology
    OPH = "oph"	 # Ophthalmology
    ORT = "ort"	 # Orthopaedic Pathology
    PME = "pme"	 # Pathology and Experimental Medicine
    PAE = "pae"	 # Pediatrics
    PHA = "pha"	 # Pharmacology
    PHI = "phi"	 # Philosophy
    PHY = "phy"	 # Physics
    PHS = "phs"	 # Physiology
    PHT = "pht"	 # Physiotherapy
    PLN = "pln"	 # Polish
    POL = "pol"	 # Political Science
    POP = "pop"	 # Population Health
    PHR = "phr"	 # Population Health Risk Assessment and Management
    POR = "por"	 # Portuguese
    PIP = "pip"	 # Pre-internship Program
    PCT = "pct"	 # Psychiatry
    PSY = "psy"	 # Psychology
    PAP = "pap"	 # Public Administration
    API = "api"	 # Public and International Affairs
    RAD = "rad"	 # Radiology
    REA = "rea"	 # Rehabilitation Sciences
    SRS = "srs"	 # Religious Studies
    RCH = "rch"	 # Research Internship
    RUS = "rus"	 # Russian Language and Culture
    SCI = "sci"	 # Science
    ISP = "isp"	 # Science, Society and Policy
    DLS = "dls"	 # Second-Language Teaching
    FSS = "fss"	 # Social Sciences
    SCS = "scs"	 # Social Sciences
    SSS = "sss"	 # Social Sciences of Health
    TSO = "tso"	 # Social Work
    SOC = "soc"	 # Sociology
    SEG = "seg"	 # Software Engineering
    ESP = "esp"	 # Spanish
    ORA = "ora"	 # Speech-Language Pathology
    SYS = "sys"	 # Systems Science
    THE = "the"	 # Theatre
    TRA = "tra"	 # Translation
    TMM = "tmm"	 # Translational and Molecular Medicine
    GLO = "glo"	 # uOGlobal
    URO = "uro"	 # Urology
    JCS = "jcs"	 # Vered Jewish Canadian Studies
    ART = "art"	 # Visual Arts
    LCM = "lcm"	 # World Literatures and Cultures
    YDD = "ydd"	 # Yiddish
