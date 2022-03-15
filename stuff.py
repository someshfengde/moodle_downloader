#%%
import requests 

dict_of_dict = {
  "CSC302\tDISCRETE STRUCTURES AND GRAPH THEORY DIV-A AY 2021-2022": {
    "Institute and Department Vision & Mission Statements File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=93233",
    "Program Outcomes(PO) File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=93235",
    "Program Educational Objectives(PEO) File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=93237",
    "Program Specific Outcomes(PSO) File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=93239",
    "Academic Calendar File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=93243",
    "PPT on Logic Part 1 (Propositions , Connectives with Truth Table) File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=93913",
    "PPT on Logic Part 2 (Rules of Logic) File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=93914",
    "More Solved Problems on Propositions File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=93917",
    "Some Solved Examples on Propositional Logic File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=93921",
    "Notes On Predicate Logic File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=94121",
    "Tautological Implications and Inference Rules and Normal Forms File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=94698",
    "Solved Examples on Mathematical Induction Part 1 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95187",
    "Solved Examples on Mathematical Induction Part 2 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95188",
    "Solved Examples on Mathematical Induction Part 3 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95189",
    "Solved Examples on Mathematical Induction Part 4 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95190",
    "Solved Examples on Mathematical Induction Part 5 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95191",
    "Introduction to Set Theory File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95192",
    "Some Examples on Basics of Set Theory File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95193",
    "Notes on Set Theory  part 1 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95194",
    "Notes on Set theory part 2 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95195",
    "Notes on Set theory part 3 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95196",
    "Notes on Set theory part 4 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95197",
    "Principle of Inclusion Exclusion File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95198",
    "Solved Problems on Principle of Inclusion Exclusion Part 1 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95203",
    "Solved Problems on Principle of Inclusion Exclusion Part 2 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95204",
    "Solved Problems on Principle of Inclusion Exclusion Part 3 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95205",
    "Solved Problems on Principle of Inclusion Exclusion Part 4 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95208",
    "Solved Problems on Principle of Inclusion Exclusion Part 5 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95209",
    "Some problems on Set Theory File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95210",
    "Some problems on Set Theory 2 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95211",
    "Problems on Set Theory 1 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95212",
    "Problems on Set Theory 2 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95213",
    "Problems on Set Theory 3 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95214",
    "Basics of Relations File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95215"
  },
  "CSC304\tDIGITAL LOGIC & COMPUTER ARCHITECTURE  DIV-A AY 2021-2022": {
    "Vision, Mission of Institute  & department File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=92019",
    "Program Educational objectives File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=92020",
    "Program Specific Outcomes File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=92021",
    "Theory Syllabus File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=92022",
    "Lab syllabus File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=92023",
    "UNIVERSITY QUESTIONS OF MODULE 1 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=94126",
    "UNIVERSITY QUESTIONS OF MODULE 2 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95738",
    "UNIVERSITY QUESTIONS OF MODULE 3.. File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97862",
    "UNIVERSITY QUESTIONS OF MODULE 4. File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97724",
    "UNIVERSITY QUESTIONS OF MODULE 5. File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97723",
    "UNIVERSITY QUESTIONS OF MODULE 6.. File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97863",
    "Assignment 1 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97259",
    "Assignment 2 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97864",
    "INTRODUCTION File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=94129",
    "Difference COCA File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=94749",
    "Introduction to Digital System Design File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=94751",
    "NumberSystem File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=94744",
    "Conversion of Number System File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=94745",
    "code conversion 1 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=94747",
    "CodeConversion 2 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=94746",
    "BCD, Grey,Excess-3, ASCII Codes File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=94752",
    "Boolean Laws and Examples File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=94748",
    "Demorgans Law File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=94750",
    "binary arithmatics , Subtraction using 1s and 2s complement File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95587",
    "BCD additon File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95583",
    "sign magnitute representation File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95588",
    "basic logic gates File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95589",
    "Derived gates File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95584",
    "Hexadecimal addition, Hexadecimal subtraction File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95585",
    "Universal gates File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95586",
    "Restoring Division Algorithm File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95734",
    "Non Restoring Division Algorithm.docx File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95736",
    "Booths algorithm for multiplication File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95735",
    "IEEE 754 representations File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95737",
    "Introduction to sequential circuit  NAND latch File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95838",
    "Half Adder  Full adder File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95839",
    "Flip Flops File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95840",
    "S-R and J-K flip flop notes compressed File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95841",
    "Addressing modes.. File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=95979",
    "Demultiplexers File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97144",
    "Multiplexers File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97145",
    "Encoders  Decoders compressed File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97146",
    "Register Organization File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97154",
    "Instruction Cycle File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97147",
    "Instruction Format and Insturction Types 1 compressed File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97149",
    "Instruction Format and Insturction Types 2continue File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97148",
    "Comparison of Hardwired  Microporgraamed Control Unit.. File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97150",
    "Hardwired Control Unit compressed compressed File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97153",
    "State Table Method File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97152",
    "Delay Element Method File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97151",
    "Microprogrammed COntrol Unit  Organization of Microprogrammed CU compressed.docx File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97731",
    "Computer Hardware COnfiguration, Microinstruction format compressed (1).docx File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97732",
    "Address sequencing (1) File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97733",
    "Microprograms File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97904",
    "Deatils of ROM compressed File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97734",
    "Characteristics of Memory compressed compressed-compressed (1) File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97735",
    "CLassification of Semiconductor memories  Details of RAM File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97736",
    "Memory Heirarchy , Cache memory, Principle of locality File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97770",
    "Cache mapping techniques File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97771",
    "Cache coherence, Interleaved memory, associative memory compressed.. File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97772",
    "SUMS ON FULLY ASSOCIATIVE CACHE MAPPING File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97958",
    "SUMS ON DIRECT CACHE MAPPING File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97959",
    "SUMS ON SE ASSOCIATIVE CACHE MAPPING compressed File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97960",
    "Pipelining, Instruction pipeline stages, performance parameters of pipelined execution compressed (1) File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97777",
    "Hazards in Instruction pipeline File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97775",
    "Flynns Classification File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97774",
    "Bus Arbitration File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97773",
    "Introduction to bus and its types, ISA, PCI, USB compressed File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97776",
    "Amdahls Law File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=97961"
  },
  "CSL405\tSKILL BASED LAB COURSE:PYTHON PROGRAMMING DIV-B AY 21-22": {
    "VISION MISSION STATEMENTS (INSTITUTE & DEPARTMENT) File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=102083",
    "PROGRAM OUTCOMES File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=102084",
    "PROGRAM EDUCATIONAL OBJECTIVES File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=102085",
    "PROGRAM SPECIFIC OUTCOMES File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=102086",
    "PYTHON LAB SYLLABUS File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=102108",
    "SUBJECT OBJECTIVE File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=102087",
    "REFERENCES File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=102091",
    "ROLL CALL LIST File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=102109",
    "Experiment List File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=103835",
    "Functions Demo File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=104026",
    "Class File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=104027",
    "Class Method and Static Method File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=104185",
    "Inheritance File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=104220",
    "Directory File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=105437",
    "Package File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=105439",
    "Module File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=105441",
    "Experiment No.3 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=105444",
    "Experiment No.5 File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=105445",
    "Regular Expressions File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=106088",
    "Single Linked List File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=106138",
    "Single Linked List-Insertion File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=106139",
    "Single Linked List-Deletion File": "http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=106140"
  }
}


for course_name , course_title in dict_of_dict.items():
    # print(course_name)
    for label,url in course_title.items():
        print(label, url)
    print("\n")
# %%

payload = {
    "username": "20102132",#20102154
    "password": "20102132@Apsit",
    "rememberusername": 1,
    "anchor": None
}


def get_session(payload):
    """
    Returns a requests.session and response 
    """
    url = "http://moodle.apsit.org.in/moodle/login/index.php"
    s = requests.session()
    r = s.post(url, data=payload)
    return s,r 


session, response = get_session(payload)
# %%
resp = session.get('http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=102083')

#%%

from bs4 import BeautifulSoup
soup=BeautifulSoup(resp.content)

relative_link = soup.find('a')['href']



# %%

session.get("http://moodle.apsit.org.in/moodle/mod/resource/view.php?id=102085")

# %%
