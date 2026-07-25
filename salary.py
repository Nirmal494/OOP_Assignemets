from employee import  AcademicEmployee
from employee import  NonAcademicEmployee

academic_emp1 = AcademicEmployee("EMP001", "Dr. Kamal Perera", 85000, 15000, 10000)
academic_emp2 = AcademicEmployee("EMP002", "Dr. Nadeesha Silva", 75000, 18000, 12000)
academic_emp3 = AcademicEmployee("EMP003", "Prof. Ruwan Jayasuriya", 90000, 14000, 10000)

nonacademic_emp1 = NonAcademicEmployee("EMP004", "Mr. Sunil Fernando", 60000, 20, 500, 7000)
nonacademic_emp2 = NonAcademicEmployee("EMP005", "Mrs. Chamari Wickramasinghe", 55000, 15, 450, 6000)
nonacademic_emp3 = NonAcademicEmployee("EMP006", "Mr. Ashan Rathnayake", 65000, 25, 550, 8000)

academic_employees = [academic_emp1, academic_emp2, academic_emp3]
nonacademic_employees = [nonacademic_emp1, nonacademic_emp2, nonacademic_emp3]

def cal_academic_salary(academic):
    tot_month_salary = 0
    tot_month_salary = tot_month_salary + academic.EmBasicSalary + academic.academicAllowance + academic.researchAllowance
    return tot_month_salary

print("---Academic Total Monthly Salary---")
for aemp in academic_employees:
    tot_salary = cal_academic_salary(aemp)
    print(f"Name: {aemp.EmName} | Id: {aemp.EmId} | Total Monthly Salary: {tot_salary}")
print()

#Total Monthly Salary = Basic Salary + (Overtime Hours × Overtime Rate) + Service Allowance
def cal_non_academic_salary(nonacademic):
    total = 0
    total= total + nonacademic.EmBasicSalary + (nonacademic.overtimeHours * nonacademic.overtimeRate) + nonacademic.serviceAllowance
    return total

print("---Non Academic Total Monthly Salary---")
for non in nonacademic_employees:
    monthly_salary = cal_non_academic_salary(non)
    print(f"Name: {non.EmName} | Id: {non.EmId} | Total Monthly Salary: {monthly_salary}")



