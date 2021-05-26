class Employee:

    # Initialize Employee object.
    def __init__(self, name, ID, department, job):
        self.__ID = ID
        self.__name = name
        self.__department = department
        self.__job = job

    # Sets employee name.
    def set_name(self, name):
        self.__name = name
    
    # Sets employee ID.
    def set_ID(self, ID):
        self.__ID = ID

    # Sets employee department.
    def set_dept(self, department):
        self.__department = department

    # Sets employee job title.
    def set_job(self, job):
        self.__job = job


    # Gets employee name.
    def get_name(self):
        return self.__name

    # Gets employee ID.
    def get_ID(self):
        return self.__ID

    # Gets employee department.
    def get_department(self):
        return self.__department

    # Gets employee Job Title.
    def get_job(self):
        return self.__job

    # Returns string of object.
    def __str__(self):
        return (f"ID Number: {self.__ID}\nName: {self.__name}\n"
                f"Department: {self.__department}\n Job Title: {self.__job}")
