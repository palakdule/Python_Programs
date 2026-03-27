import pandas as pd
import os

def employee_analysis():
    file_name = 'employee.xlsx'
    data = {'Employee ID': [101, 102, 103, 104, 105], 'Employee Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'], 'Department': ['Automotive', 'Healthcare', 'Automotive', 'Finance', 'Automotive'], 'Designation': ['Developer', 'Manager', 'Developer', 'Analyst', 'Senior Developer']}
    df_dummy = pd.DataFrame(data)
    try:
        df_dummy.to_excel(file_name, index=False)
        print(f"Sample '{file_name}' created successfully.")
    except exception as e:
        print(f"Error creating '{file_name}': {e}")
        file_name = 'employee.csv'
        df_dummy.to_csv(file_name, index=False)
        print(f"Fallback to '{file_name}' created successfully.")
    try:
        if file_name.endswith('.xlsx'):
            df = pd.read_excel(file_name)
        else:
            df = pd.read_csv(file_name)
    except exception as e:
        print(f'Error reading file: {e}')
        return
    print('\n--- a) Employees in Automotive Domain ---')
    automotive_employees = df[df['Department'] == 'Automotive']
    print(automotive_employees.to_string(index=False))
    emp_id = 102
    print(f'\n--- b) Details for Employee ID: {emp_id} ---')
    emp_details = df[df['Employee ID'] == emp_id]
    if not emp_details.empty:
        print(emp_details.to_string(index=False))
    else:
        print(f'Employee with ID {emp_id} not found.')
    print('\n--- c) List of all Developers ---')
    developers = df[df['Designation'].str.contains('Developer')]
    print(developers.to_string(index=False))
if __name__ == '__main__':
    employee_analysis()