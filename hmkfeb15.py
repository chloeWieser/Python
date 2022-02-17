import pickle

# #You will write a command line program to manage a phone book. When you start the phonebook.py program, it will print out a menu and ask the user to enter a choice:



file_name = "myPhonebook.pickle" #I manually created a file called myPhonebook.pickle- see Veronicas method below

myPhonebook = {
        "Name": "Number"
    }

with open("myPhonebook.pickle", 'rb') as file_handle: #means if myPhonebook.pickle does exist, get all the info from it
    myPhonebook = pickle.load(file_handle)
    

getTask = True

while getTask:
    selection = int(input(f"""
    Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit

    What do you want to do (1-5)?
    """))


    if selection == 1: # Look up an entry
    
        Name = input("Name: ")
        #look up person's phone number by given name and print to screen
        Result = myPhonebook.get(Name)
        print(f"""
    Name: {Name}
    Found entry for {Name}: {Result}
    """)
    elif selection == 2: 
        newEntry = input("Name: ")
        newNumber = input("Phone Number: ")
        myPhonebook[newEntry] = newNumber #adding and setting the value and the key for the new entry
        print(f"Entry stored for {newEntry}.")
    elif selection == 3: 
        deleteEntry = input("Name: ")
        del myPhonebook[deleteEntry]
    elif selection == 4: 
        for Name, Number in myPhonebook.items():
            print(f"{Name}\t\t{Number}")
            
    elif selection == 5:
        getTask=False
        print("Bye")
        
        with open('myPhonebook.pickle', 'wb') as file_handle: 
            pickle.dump(myPhonebook, file_handle)


# -----Veronica's solution-------

import pickle #imports in module that allows your to export data to .pickle file 

try: 
    with open('phonebook.pickle', 'rb') as fh: #means try to open this file if it exists (on the server?)
        phonebook = pickle.load(fh)  #if it does exist, get all the info from it
except: 
    phonebook = {}#otherwise create this new file

# phonebook = {}  # global variable 

# {
#     "Anna": "333-333-3333"
# }

def searchName():
    print(f''' 
Search Contacts
======================   
''')
    name = input('Search for a name >> ') #Melissa
    
    if name in phonebook:
        print(f'{name} {phonebook[name]}')
    else:
        print('Contact not found')

def addContact(): 
    name = input('Enter a name >> ')  #Anna
    phoneNumber = input('Enter a phone number >> ') #333-333-3333
    
    phonebook[name] = phoneNumber

def deleteContact():
    print(f''' 
Delete Contacts
======================   
''')
    name = input('insert a name to delete >>') # Melissa
    
    if name in phonebook: 
        del phonebook[name]
    else: 
        print('no contact to delete')

def listAllEntries():
    print(f''' 
Phone Book Contacts
======================   
''')
    
    for name, phonenumber in phonebook.items(): # [("Anna", "333-333-3333"), ()]
        print(f'{name}\t\t{phonenumber}')


def menu():                  #----veronica started here and then went back up to define the functions needed within each if statement below
    selection = int(input(""" 
Electronic Phone Book
======================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Exit                     
"""))
    return selection 


endProgram = False   #knowing that she'll have an option to endProgram (#5), she's saying to make the loop keep going endProgram ntb False

while not endProgram: #so while endProgram is TRUE (like not False, per the variable), take the user through this loop
    
    selection = menu()
    
    if selection == 1: 
        searchName()
    elif selection == 2: 
        addContact()
    elif selection == 3: 
        deleteContact() 
    elif selection == 4: 
        listAllEntries() 
    elif selection == 5: 
        endProgram = True   #this sets endProgram to be True, so since the while loop requires endProgram to be FALSE, that means While loop statement, 'while not endProgram' is now FALSE(Becasue endProgram != False per the original variable)- so the program ends i/o going through the loop
        with open('phonebook.pickle', 'wb') as fh:
            pickle.dump(phonebook, fh)  #means update and save the pickle file with any new info