from pyscript import display, document

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return(f"Hi! My name is {self.name}. I am from section {self.section}, and my favorite subject is {self.favorite_subject}.")

classmates = [ 
    Classmate("Queeny", "Ruby", "English"),
    Classmate("Sam", "Ruby", "Science"), 
    Classmate("Samantha", "Ruby", "Math"),  
    Classmate("Ashley", "Ruby", "Social Studies"), 
    Classmate("Meyer", "Ruby", "PE") 
]

def add_classmate(e):
    document.getElementById("output").innerHTML = "" 

    # Check validation
    name_val = document.getElementById("name").value
    sec_val = document.getElementById("section").value
    sub_val = document.getElementById("favorite_subject").value

    if name_val == "" or sec_val == "" or sub_val == "": 
        display("Please fill in all fields.", target="output") 
        return

    # Add information to list
    classmates.append(Classmate(name_val, sec_val, sub_val))

    # Show success message
    display(f"✅ Classmate '{name_val}' added successfully!", target="output")

def show_list(e):
    document.getElementById("output").innerHTML = "" 
    for c in classmates: 
        display(c.introduce(), target="output")

