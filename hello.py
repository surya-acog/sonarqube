from drills import Employee,Project,Department
from typing import List,Dict

class Company():

    def __init__(self,company_name: str) -> None:
        self.company_name = company_name
        self.departments: List[Department] = []
        self.projects: List[Project] = []
        self.employees: List[Employee] = []
    
    def add_department(self,department_name: str, employee_name: str, employee_id: str, employee_position: str, employee_salary: str) -> None:
        '''add a department to the company'''
        dept_object = Department(department_name: str,employee_name: str, employee_id: str, employee_position: str, employee_salary: int)
        self.departments.append(dept_object)

    def add_project(self,project_name: str) -> None:
        '''add a project to the company'''
        self.projects.append(Project(project_name))

    def add_employee(self,employee_name: str,employee_id: str,employee_position: str,employee_department: str, employee_salary: int) -> None:
        '''add an  employee to the company'''
        self.employees.append(Employee(employee_name,employee_id,employee_position,employee_department,employee_salary))

    def department_summary(self,department_name: str) -> Dict[str, List[Employee]]:
        ''' provide the summary of employees in a department'''
        return Department.department_info[department_name]
    
    def project_summary(self,project_name: str) -> Dict[str,List[Employee]] :
        ''' provide the summary of employee in a project'''
        return Project.project_info[project_name]
    
if __name__ == "__main__":
    company_object: Company = Company("Aganitha")
