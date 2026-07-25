class Employee:
    def __init__(self, emId, emName, emBasicSalary):
        self.EmId = emId
        self.EmName = emName
        self.EmBasicSalary = emBasicSalary

class AcademicEmployee(Employee):
    def __init__(self, emId, emName, emBasicSalary, academicAllowance, researchAllowance):
        super().__init__(emId, emName, emBasicSalary)
        self.academicAllowance = academicAllowance
        self.researchAllowance = researchAllowance



class NonAcademicEmployee(Employee):
    def __init__(self, emId, emName, emBasicSalary, overtimeHours, overtimeRate, serviceAllowance):
        super().__init__(emId, emName, emBasicSalary)
        self.overtimeHours = overtimeHours
        self.overtimeRate = overtimeRate
        self.serviceAllowance = serviceAllowance
