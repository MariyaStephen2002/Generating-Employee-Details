class employee:
  def __init__(Self,Name,Id,Salary):
    Self.employee_name=Name
    Self.employee_id=Id
    Self.employee_salary=Salary
  def sal_with_flt(Self):
    Self.employee_salary1=format(Self.employee_salary,".2f")
  def name_split(Self):
   Self.Emp_first_name, Self.Emp_last_name = Self.employee_name.split()
  def sal_with_pf_details(Self):
    Self.employee_salary1=int(Self.employee_salary-((Self.employee_salary/100)*10))
  def Anual_Sal(Self):
    Self.employee_salary1=Self.employee_salary*12

class TCS(employee):
  def show(Self):
    print("Name:",Self.employee_name,"\nID: TCS"+str(Self.employee_id),"\nSalary:",Self.employee_salary1,"\nLocation:",Self.location,"\nDOB:",Self.dob)
  def update(Tcs,Location, DOB):
    Tcs.location=Location
    Tcs.dob=DOB

class HCL(employee):
  def show(Self):
    print("First Name:",Self.Emp_first_name,"\nLast Name:",Self.Emp_last_name,"\nID: HCL"+str(Self.employee_id),"\nSalary:",Self.employee_salary1,"\nGender:",Self.gender,"\nBlood Group:",Self.bloof_group,"\nDate Of Joining:",Self.doj)
  def update(Hcl,Gender, Blood_Group, DOJ):
    Hcl.gender=Gender
    Hcl.bloof_group=Blood_Group
    Hcl.doj=DOJ

class ZOHO(employee):
  def show(Self):
    print("Name:",Self.employee_name,"\nID: ZOHO"+str(Self.employee_id),"\nLPA:",Self.employee_salary1,"\nExperience:",Self.experience,"\nMobile Number:",Self.mobile,"\nAddress:",Self.address,"\nAadhar Number:",Self.aadhar)
  def update(Zoho,Experience, Mobile, Address, Aadhar):
    Zoho.experience=Experience
    Zoho.mobile=Mobile
    Zoho.address=Address
    Zoho.aadhar=Aadhar

Employee1=TCS("raj S",55176,40000)
Employee2=HCL("reena Rose",55609,40000)
Employee3=ZOHO("maran S",55170,40000)

Employee1.sal_with_flt()

Employee1.update("Puducherry","10/10/1995")

Employee1.show()

Employee2.name_split()

Employee2.sal_with_pf_details()

Employee2.update("Male","O+","10/10/2018")

Employee2.show()

Employee3.Anual_Sal()

Employee3.update(4,"9500691867","NO: 92, Kamaraj Salai, Chennai - 70", 638060344554)

Employee3.show()
