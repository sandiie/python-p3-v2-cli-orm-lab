from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
     employees = Employee.get_all()
     for employee in employees:
        print(employee)
     pass


def find_employee_by_name():
     name = input("Enter the employee's name: ")
     employee = Employee.find_by_name(name)
     print(employee) if employee else print(
        f'Employee {name} not found')

     pass


def find_employee_by_id():
    employee_id = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(employee_id):
        print(employee)
    else:
        print(f'Employee {employee_id} not found')
    pass


def create_employee():
    print("Enter Employee Details:")
    name = input("Name: ")
    position = input("Position: ")
    employee = Employee(name, position,)
    employee.save()
    print("Employee Created Successfully")
    pass


def update_employee():
     id_ = input("Enter the department's id: ")
     if employee := Employee.find_by_id(id_):
        try:
            name = input("Enter the employee's new name: ")
            employee.name = name
            location = input("Enter the employee's new location: ")
            employee.location = location

            employee.update()
            print(f'Success: {employee}')
        except Exception as exc:
            print("Error updating employee: ", exc)
     else:
        print(f'Employee {id_} not found')


     pass


def delete_employee():
    employee_id = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(employee_id):
        employee.delete()
        print(f'Employee {employee_id} deleted')
    else:
        print(f'Employee {employee_id} not found')
    pass


def list_department_employees():
    department_id = input("Enter the department's id: ")
    department = Department.find_by_id(department_id)
    if department:
        employees = Employee.get_all_by_department(department_id)
        for employee in employees:
            print(employee)
    else:
        print(f'Department {department_id} not found')
    pass