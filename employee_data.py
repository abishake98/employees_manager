#Employee ID
def read_employee_id():
    while True:
        employee_id_str = input("Please Enter Your Employee ID: ")
        if employee_id_str.isdigit():
            employee_id = int(employee_id_str)
            return employee_id
        else:
            print("WARNING: Please Enter a Valid Employee ID")

#employee_id = read_employee_id()

#First Name
def read_first_name():
    while True:
        first_name = input("Please Enter Your First Name: ")

        if len(first_name.strip()) >= 2:
            return first_name

        else:
            print("WARNING: Please Enter a Valid First Name")

#first_name = read_first_name()

#Last Name
def read_last_name():
    while True:
        last_name = input("Please Enter Your Last Name: ")

        if len(last_name.strip()) >= 2:
            return last_name

        else:
            print("WARNING: Please Enter a Valid Last Name")

#last_name = read_last_name()

#Birthyear
def read_birth_year():
    while True:
        birth_year_str = input("Please Enter Your Year of Birth: ")
        if birth_year_str.isdigit():
            birth_year = int(birth_year_str)
            if (birth_year >= 1900) and (birth_year <= 2004):
                return birth_year
            else:
                print("WARNING: Please Enter a Valid Year of Birth")

        else:
            print("WARNING: Please Enter a Valid Year of Birth")

#birth_year = read_birth_year()

#Birthmonth
def read_birth_month():
    while True:
        birth_month_str = input("Please Enter Your Month of Birth, as a Number: ")
        if birth_month_str.isdigit():
            birth_month = int(birth_month_str)
            if (birth_month >= 1) and (birth_month <= 12):
                return birth_month
            else:
                print("WARNING: Please Enter a Valid Month of Birth")

        else:
            print("WARNING: Please Enter a Valid Month of Birth")

#birth_month = read_birth_month()

#Birthday
def read_birth_day():
    while True:
        birth_day_str = input("Please Enter Your Day of Birth: ")
        if birth_day_str.isdigit():
            birth_day = int(birth_day_str)
            if (birth_day >= 1) and (birth_day <= 31):
                return birth_day
            else:
                print("WARNING: Please Enter a Valid Day of Birth")

        else:
            print("WARNING: Please Enter a Valid Day of Birth")

#birth_day = read_birth_day()

#Postion
def read_position():
    position = input("Please State Your Position in This Company: ")
    if len(position.strip()) > 0:
        return position

    else:
        print("Please Enter a Valid Position of Responsibility")

#position = read_position()

#Graduated from university?
def read_graduation():
    while True:
        graduation = input("Did You Graduate From a University? (yes/no) ")
        if graduation == "yes":
            return graduation
        elif graduation == "no":
            return graduation
        else:
            print("WARNING: Please Enter Either yes or no")

#graduation = read_graduation()

def add_employee():
    first_name = read_first_name()
    last_name = read_last_name()
    birth_day = read_birth_day()
    birth_month = read_birth_month()
    birth_year = read_birth_year()
    position = read_position()
    graduation = read_graduation()
    employee = {"Employee First Name" : first_name,
                "Employee Last Name" : last_name,
                "Birth Day" : birth_day,
                "Birth Month" : birth_month,
                "Birth Year" : birth_year,
                "Position of Responsibility" : position,
                "Graduated?" : graduation}

    return employee

def read_remove_employee_id():
    while True:
        remove_id_str = input("Which Employee ID Would You Like to Remove From the System? ")
        if remove_id_str.isdigit():
            remove_id = int(remove_id_str)
            return remove_id
        else:
            print("WARNING: Enter a Valid Employee ID")

def read_view_employee_id():
    while True:
        view_id_str = input("Which Employee ID Would You Like to View From the System? ")
        if view_id_str.isdigit():
            view_id = int(view_id_str)
            return view_id
        else:
            print("WARNING: Enter a Valid Employee ID")

def read_modify_employee_id():
    while True:
        modify_id_str = input("Which Employee ID Would You Like to Modify From the System? ")
        if modify_id_str.isdigit():
            modify_id = int(modify_id_str)
            return modify_id
        else:
            print("WARNING: Enter a Valid Employee ID")
