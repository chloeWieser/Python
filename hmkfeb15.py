import pickle

# #You will write a command line program to manage a phone book. When you start the phonebook.py program, it will print out a menu and ask the user to enter a choice:


file_name = "myPhonebook.pickle"

myPhonebook = {
        "Name": "Number"
    }

with open("myPhonebook.pickle", 'rb') as file_handle: 
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

