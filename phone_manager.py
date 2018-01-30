# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones


class Phone():

    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None

    def assign(self, employee_id):
        self.employee_id = employee_id

    def is_assigned(self):
        return self.employee_id is not None

    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model, self.employee_id)


class Employee():

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)


class PhoneAssignments():

    def __init__(self):
        self.phones = []
        self.employees = []

    def add_employee(self, employee):
        # raise exception if two employees with same ID are added
        for person in self.employees:
            if person.id == employee.id:
                raise PhoneError
        self.employees.append(employee)

    def add_phone(self, phone):
        # raise exception if two phones with same ID are added
        for mobile in self.phones:
            if mobile.id == phone.id:
                raise PhoneError
        self.phones.append(phone)

    def assign(self, phone_id, employee):
        # Find phone in phones list
        # if phone is already assigned to an employee, do not change list, raise exception
        # if employee already has a phone, do not change list, and raise exception
        if employee.id in [phone.employee_id for phone in self.phones]:
            raise PhoneError
        # if employee already has this phone, don't make any changes. This should NOT raise an exception.
        else:
            for phone in self.phones:
                if phone.employee_id is not None:
                    raise PhoneError
                if phone.id == phone_id:
                    if phone.employee_id != employee.id:
                        phone.assign(employee.id)
                    else:
                        print('Phone was already assigned to Employee')

    def un_assign(self, phone_id):
        # Find phone in list, set employee_id to None
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)   # Assign to None

    def phone_info(self, employee):
        # find phone for employee in phones list

        # return None if the employee does not have a phone
        # raise an exception if the employee does not exist

        for phone in self.phones:
            if employee not in self.employees:
                raise LookupError
            elif phone.employee_id not in [employee.id for employee in self.employees]:
                return None
            else:
                if phone.employee_id == employee.id:
                    return phone

        return None


class PhoneError(Exception):
    pass

