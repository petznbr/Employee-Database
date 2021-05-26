# Libraries to import.
import pickle
import emp

def main():
    # Try to open the existing dictionary file
    try:
        inputFile1 = open('employee.pickle', 'rb')
        employeeDictionary = pickle.load(inputFile1)
        inputFile1.close()
        inputFile2 = open('deletedEmployee.pickle', 'rb')
        deletedEmployeeDictionary = pickle.load(inputFile2)
        inputFile2.close()
    
    #If no dictionary exists create empty dictionary.
    except:
        employeeDictionary = {}
        deletedEmployeeDictionary = {}

   # While loop to continue until user chooses to quit
    proceed = True
    while proceed:

        # Display user's option menu and ask for a choice
        print('\n Employee Management System\n')
        print('\t1. Lookup an employee')
        print('\t2. Add a new employee')
        print('\t3. Change an employee')
        print('\t4. Delete an existing employee')
        print('\t5. Move a deleted employee back to active')
        print('\t6. Save and Quit\n')
        
        # Stores choice.
        choice = int(input('Enter an option to continue: '))
        while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6:
            choice = int(input('ERROE! Enter a valid option to continue: '))
        # If loop to decide what to do with choice.
        if choice == 1:
            lookup (employeeDictionary, deletedEmployeeDictionary)
        elif choice ==2:
            add(employeeDictionary, deletedEmployeeDictionary)
        elif choice == 3:
            change (employeeDictionary, deletedEmployeeDictionary)
        elif choice == 4:
            delete (employeeDictionary, deletedEmployeeDictionary)
        elif choice == 5:
            activate(deletedEmployeeDictionary, employeeDictionary)
        else:
            save_quit(employeeDictionary, deletedEmployeeDictionary)
            proceed = False

# Lookup an employee
def lookup(dictionary, dictionary2):
    # Look up the ID number if it is in the active employee dictionary.
    employee_id = int(input('Enter the employee ID number: '))
    if employee_id in dictionary:
        # print('employee_id', ': ', dictionary[employee_id])
        print(dictionary.get(employee_id))
        # Prints out to conform employee is active.
        print('This employee is active!')
    # Look up the ID number if it is in the inactive(deleted) employee dictionary.
    elif employee_id in dictionary2:
        # print('employee_id', ': ', dictionary2[employee_id])
        print(dictionary2.get(employee_id))
        # Prints out to conform employee is inactive.
        print('This employee is inactive!')
    else:
        # Prints out to conform employee does not exist.
        print('Employee ID was not found!')


# Add an employee
def add(dictionary, dictionary2):
    # Add a new employee to active dictionary.
    employee_id = int(input('Enter the employee ID number: '))
    # Checks to make sure employee ID does not already exist.
    if employee_id not in dictionary.keys() or employee_id not in dictionary2.keys():
        name = input('Enter the name of the employee: ')
        dept = input('Enter the employee department: ')
        job = input('Enter the employee job title: ')
        entry = emp.Employee(name, employee_id, dept, job)
        dictionary[employee_id] = entry
        print('Employee added succesfully')
    else:
        # Prints if employee ID already exists.
        print('Employee ID already exists!')

# Change an employee
def change(dictionary, dictionary2):
    # If employee is in either dictionary, allow them to change the info.
    employee_id = int(input(
        'Enter the employee ID you would like to change: '))
    # Checks if employee is deleted.
    if employee_id in dictionary2.keys():
        # If employee is deleted check if user wants to update information.
        choice = input('Do you want to update a deleted record? (y/n): ')
        # Runs until user enters y or n.
        while choice.lower() != 'y' and choice.lower() != 'n':
            choice = input('ERROR! Invalid input! (y/n): ')
        # Runs if user wants to update deleted employee.
        if choice.lower() == 'y':
            name = input('Enter new employee name: ')
            dept = input('Enter new employee department: ')
            job = input('Enter new employee job title: ')
            entry = emp.Employee(name, employee_id, dept, job)
            dictionary2[employee_id] = entry
            print('Employee changed successfully.')
        # Prints if user enters n.
        else:
            print('Employee information not updated!')
    # If employee is not deleted if employee exists in employee dictionary.
    elif employee_id in dictionary.keys():
        name = input('Enter new employee name: ')
        dept = input('Enter new employee department: ')
        job = input('Enter new employee job title: ')
        entry = emp.Employee(name, employee_id, dept, job)
        dictionary[employee_id] = entry
        print('Employee changed successfully.')
    else:
        # Prints if no such employee exists.
        print('Employee ID was not found!')
        
def move(dictionary, dictionary2, employee_id):
    # Copies selected employee from employee dictionary to deleted dictionary.
    dictionary2[employee_id] = dictionary.get(employee_id)

# Delete an employee
def delete(dictionary, dictionary2):
    # If user-entered ID is in dictionary, move to delete dictionary and dlete in employee dictionary.
    employee_id = int(input(
        'Enter the employee ID you would like to remove: '))
    if employee_id in dictionary.keys():
        # Move employee to delete dictionary.
        move(dictionary, dictionary2, employee_id)
        # Remove employee from employee dictionary.
        dictionary.pop(employee_id)
        # Prints out when done.
        print('Employee successfully moved to deleted dictionary!')
    else:
        # Prints if employee is not in employee dictionary.
        print('Employee ID was not found!')
        
def activate(dictionary, dictionary2):
    # If employee is in delete dictionary, allow user to move them back to standard employee dictionary.
    employee_id = int(input(
        'Enter the employee ID you would like to reactivate: '))
    if employee_id in dictionary.keys():
        # Move employee to delete dictionary.
        move(dictionary, dictionary2, employee_id)
        dictionary.pop(employee_id)
        # Prints out when done.
        print('Employee successfully reactivated!')
    else:
        print('Employee ID was not found!')
        

# Save the dictionary and quit the program
def save_quit(dictionary, dictionary2):
    # Pickle the employee dictionary and save to a file
    outputFile1 = open('employee.pickle', 'wb')
    pickle.dump(dictionary, outputFile1)
    # Close file.
    outputFile1.close
    # Pickle the delete dictionary and save to a file
    outputFile2 = open('deletedEmployee.pickle', 'wb')
    pickle.dump(dictionary2, outputFile2)
    # Close file.
    outputFile2.close
    
#Calls main function.   
if __name__== '__main__':
    main()
