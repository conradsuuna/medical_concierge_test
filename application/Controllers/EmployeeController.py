from ..Models.employee import Employee
from ..Models.employee_designation import Designation  
import os
from .. import session

def add_employee_data():
    employee_data=[
        Employee(name='Nabimanya Nelson John Paul',staff_status='active',
            role='Editor',time_spent_status='new'),
        Employee(name='Kenneth Ojakol',staff_status='active',
            role=None,time_spent_status='new'),
        Employee(name='Thomas Kyamagero',staff_status='pending',
            role='Admin',time_spent_status='new'),
        Employee(name='Paul Nabimanya',staff_status='active',
            role='Viewer',time_spent_status='old'),
        Employee(name='Kyamagero Paul',staff_status='active',
            role='Admin',time_spent_status='new'),
        Employee(name='SSali Peter',staff_status='active',
            role=None,time_spent_status='new'),
        Employee(name='Zizinga Pius',staff_status='active',
            role='Viewer',time_spent_status='new'),
        Employee(name='Jalia Nabukalu Esther',staff_status='pending',
            role='Admin',time_spent_status='new'),
        Employee(name='John Zizinga',staff_status='pending',
            role=None,time_spent_status='new'),
        Employee(name='Sharon Opoka',staff_status='active',
            role='Editor',time_spent_status='new'),
        Employee(name='Nabimanya Paul',staff_status='active',
            role=None,time_spent_status='new'),
        Employee(name='Ojakol Kenneth',staff_status='active',
            role=None,time_spent_status='new'),
        Employee(name='Opoka Jane Sharon',staff_status='active',
            role='Editor',time_spent_status='new'),
        Employee(name='Kikoyo Paul',staff_status='active',
            role=None,time_spent_status='new'),
        Employee(name='Esther Nabukalu',staff_status='active',
            role=None,time_spent_status='new'),
    ]
    for employee in employee_data:
        employee.save()
    print('saved successfully')
    return


def add_designation_data():
    designation_data=[
        Designation(employee_id=1,designation_type='Manager'),
        Designation(employee_id=2,designation_type='Backend developer'),
        Designation(employee_id=3,designation_type='Accountant'),
        Designation(employee_id=4,designation_type='Director of operations'),
        Designation(employee_id=5,designation_type='Network manager'),
        Designation(employee_id=6,designation_type='I.T team lead'),
        Designation(employee_id=7,designation_type='Finance manager'),
        Designation(employee_id=8,designation_type='Systems admin Intern'),
        Designation(employee_id=9,designation_type='Backend developer'),
        Designation(employee_id=10,designation_type='Communications manager'),
        Designation(employee_id=11,designation_type='Assistant director of operations'),
        Designation(employee_id=12,designation_type='Backend developer'),
        Designation(employee_id=13,designation_type='General caretaker'),
        Designation(employee_id=14,designation_type='Frontend developer'),
        Designation(employee_id=15,designation_type='graphics designer'),
    ]
    for designation in designation_data:
        designation.save()
    print('successfully saved')
    return


# function to render html views
def render_template(template_name, context):
    html_string = ""
    with open(template_name, 'r') as file_z:
        html_string = file_z.read()
        # html_str = html_str.format(**context) #unpack context
    return html_string


def show_employees(environ):
    # session.query(Employee).delete()
    # session.query(Designation).delete()
    # session.rollback()
    employee_count = session.query(Employee).count()
    designation_count = session.query(Designation).count()
    # print(employee_count)
    # print(designation_count)

    # prevent double entries
    if employee_count < 15 and designation_count < 15:
        try:
            add_employee_data()
            add_designation_data()
        except:
            session.rollback()
            raise
        finally:
            session.close()
    cwd = os.getcwd() # current working directory
    return render_template(
        template_name = cwd+'/application/Views/employees.html', 
        context={}
    )

def get_employee_data():
    # get data from db
    employees = []
    employee_data = [z.to_json() for z in session.query(Employee).all()]
    for row in employee_data:
        row['designation_type'] = session.query(Designation)\
            .filter(Designation.employee_id==row['id'])[0].designation_type
        employees.append(row)
    return employees
