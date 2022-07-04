#Generate personal details form with idea of Application letter to a tech companies like GOOGLE. 

# giving simple Personal Details about the user 
name = input ("Input your full name: ")
address = input ("Input your full address: ")
job_title = input ("Input your job title: ") 
phone_no = input ("Input your Phone no: ")
email_address = input ("Input your email address: ")
birth_year = int(input ("Input your Birth year: "))
marital_status = input ("What is your marital status? ")
sex = input ("What is your gender?,. M/F: ")
manager_name = input ("Hiring Manager's name: ")
age = 2022 - birth_year

def personal_details():
    print ("SUBMIT YOUR PERSONAL DETAILS; ".center(50))
    print ("Name: ".ljust(17, "_"), name.upper() )
    print ("Age: ".ljust(26, "_"), age)
    print ("Home Address: ".ljust(17, "_"), address.upper())
    print ("Job Title: ".ljust(17, "_"), job_title.upper())
    print ("Active Phone number: ".ljust(15, "_"), phone_no)
    print ("Email Address: ".ljust(17, "_"), email_address)
    print ("Sex: ".ljust(26, "_"), sex)
    print ("Marital status: ".ljust(17, "_"), marital_status.upper())
#calling the personal details. 
personal_details()

print ("""        


""")

#The Application letter's body. 
def application_letter():
    print ("Dear,", manager_name)
    print ("""    I have been modeling data ever since I won a young data scientist prize aged 15. That winning the project analyzed how a teenager’s Google activity can impact their future life choices. Fifteen years later, I am wondering about how I might make an impact at Google. 
    Having delayed my entry into corporate life longer than most after two years interning for a data-modeling consultancy, and after receiving my master's in data science from Penn State, I undertook a two-year research assignment with the U.S. government to work on their digital citizen project. These people-led behavioral insights will come in useful in the role at Google and I enclose two whitepapers that will shed some light on the “psychology of choice” and how data informs online design.
    At ANY-CHOICE BET, I spent four years creating algorithms and decision-making engines for an online betting company, increasing profits by 35%, retaining 24% more players, and increasing game time by over 44% per player in their first 90 days. Analyzing the data of why people stayed engaged was complex with an 18 million-strong player base.
    My work on a machine learning application for the U.S. postal service led to operational efficiencies and savings of $30m+ - ensuring that their vast resources were optimized and that swings in activity were easier to manage. The data contradicted 40% of the conventional wisdom, necessitating influencing at the highest levels of the organization.
    I am used to explaining my work and communicating with the most senior stakeholders and believe that without their understanding, any data insights are wasted.
    I would welcome an interview to discuss the parameters of the role – the opportunity to work on the behavioural analysis team is a unique challenge for any """, job_title.upper(),""" .


Sincerely,""",

name.upper(),  """.
""")

application_letter()