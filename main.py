import employee_data
print("-----------------------------------------")
print("WELCOME TO THE EMPLOYEE MANAGEMENT SYSTEM")
print("-----------------------------------------")

Total_Number_Employees = 0

employees = {}

while True:
    print("What would you like to do? ")
    print("-----------------------------------------")

    print("1) Add an Employee")
    print("-----------------------------------------")
    print("2) Remove an Employee")
    print("-----------------------------------------")
    print("3) Get Total Number of Employees")
    print("-----------------------------------------")
    print("4) Get List of All Employees")
    print("-----------------------------------------")
    print("5) Retrieve the Data of an Employee (by Employee ID)")
    print("-----------------------------------------")
    print("6) Update the Data of an Employee")
    print("-----------------------------------------")
    print("7) Exit")
    print("-----------------------------------------")

    choice = input("Please Select One of the Above Options (1/2/3/4/5/6/7): ")
    # Add an Employee
    if choice == "1":
        Total_Number_Employees = Total_Number_Employees + 1
        employee_id = employee_data.read_employee_id()
        new_employee = employee_data.add_employee()
        employees[employee_id] = new_employee

        print(new_employee)
        print("Employee Successfully Added")

    # Remove an Employee
    elif choice == "2":
        if Total_Number_Employees == 0:
            print("Unable to Remove Employee")

        else:
            Total_Number_Employees = Total_Number_Employees - 1
            remove_id = employee_data.read_remove_employee_id()
            del employees[remove_id]

            print("Employee Succesfully Removed")

    # Get Total Number of Employees
    elif choice == "3":
        print(f"Total Number of Employees: {Total_Number_Employees}")

    # Get List of All Employees
    elif choice == "4":
        print(employees)

    # Get Total Number of Employees
    elif choice == "4":
        print(f"Total Number of Employees: {Total_Number_Employees}")

    # Retrieve the Data of an Employee (by Employee ID)
    elif choice == "5":
        view_id = employee_data.read_view_employee_id()

        view_employee = employees[employee_id]

        print(view_employee)

    # Update the Data of an Employee
    elif choice == "6":
        modify_id = employee_data.read_modify_employee_id()

        while True:

            view_employee = employees[modify_id]
            print("-----------------------------------------")
            print(view_employee)
            print("-----------------------------------------")
            print("What Would You Like to Update For This Employee?")
            print("1) Employee First Name")
            print("2) Employee Last Name")
            print("3) Birth Day")
            print("4) Birth Month")
            print("5) Birth Year")
            print("6) Position of Responsibility")
            print("7) Graduated?")
            print("8) Back to Menu")


            modification = input("Please Select One From the Above Options (1/2/3/4/5/6/7/8): ")

            if modification == "1":

                modify_first_name = employee_data.read_first_name()

                view_employee["Employee First Name"] = modify_first_name

                print(view_employee)

            elif modification == "2":

                modify_last_name = employee_data.read_last_name()

                view_employee["Employee Last Name"] = modify_last_name

                print(view_employee)

            elif modification == "3":

                modify_birth_day = employee_data.read_birth_day()

                view_employee["Birth Day"] = modify_birth_day

                print(view_employee)

            elif modification == "4":

                modify_birth_month = employee_data.read_birth_month()

                view_employee["Birth Month"] = modify_birth_month

                print(view_employee)

            elif modification == "5":

                modify_birth_year = employee_data.read_birth_year()

                view_employee["Birth Year"] = modify_birth_year

                print(view_employee)

            elif modification == "6":

                modify_position = employee_data.read_position()

                view_employee["Position of Responsibility"] = modify_position

                print(view_employee)

            elif modification == "7":

                modify_graduation = employee_data.read_graduation()

                view_employee["Graduated?"] = modify_graduation

                print(view_employee)

            elif modification == "8":
                break

            else:
                print("Warning: Invalid Option! Please Try Again")


    # Exit
    elif choice == "7":
        print("-----------------------------------------")
        print("Thank you for using the Employee Management System")
        print("-----------------------------------------")
        break

    else:
        print("Warning: Invalid Option! Please Try Again")