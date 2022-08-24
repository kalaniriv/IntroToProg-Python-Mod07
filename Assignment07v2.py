# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# Krivera, 2022-08-22,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
objFile = None
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    objFile = open(strFileName, 'wb')
    pickle.dump(lstCustomer, objFile)
    objFile.close()

def read_data_from_file(file_name):
    objFile = open(strFileName, 'rb')
    lstCustomer = pickle.load(objFile)
    objFile.close()
    return lstCustomer

def get_user_choice():
    choice = str(input('\nWould you like to add an entry? (Y/N): ')).strip()
    print()
    return choice

def get_user_input():
    id = input('Enter an ID to add to the list: ')
    name = input('Enter a name associated with the ID: ')
    lstCustomer = [id, name]
    return lstCustomer

def add_data_to_list(id, name, lstCustomer):
    row = [id, name]
    lstCustomer.append(row)
    return lstCustomer

# Presentation ------------------------------------ #
# TODO: Get ID and NAME From user, then store it in a list object
while (True):
    choice_str = get_user_choice()
    if choice_str.lower() == 'y':
        id, name = get_user_input()
        add_data_to_list(id, name, lstCustomer)
        save_data_to_file(objFile, lstCustomer)
        print('\nNew entry added to list')
    elif choice_str.lower() == 'n':
        break
    else:
        print('Please enter a valid selection: "y" or "n": ')

# TODO: store the list object into a binary file
save_data_to_file(objFile, lstCustomer)
print('Data saved \nPress enter to read the data from the file and display the contents')
input()

# TODO: Read the data from the file into a new list object and display the contents
read_data_from_file(objFile)
print(lstCustomer)
print('Press enter to exit')