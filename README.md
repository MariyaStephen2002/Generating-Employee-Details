









Certainly! The program you provided is a Python script that defines three classes: `Employee`, `TCS`, `HCL`, and `ZOHO`. These classes are used to create different types of employees (TCS, HCL, ZOHO) with specific attributes and methods. Here's a breakdown of the program:

### Class Definitions:

#### 1. `Employee` Class:
- **Attributes**: `employee_name`, `employee_id`, `employee_salary`
- **Methods**:
    - `sal_with_flt()`: Formats the `employee_salary` to two decimal places.
    - `name_split()`: Splits the `employee_name` into first and last names.
    - `sal_with_pf_details()`: Reduces the salary by 10%.
    - `Anual_Sal()`: Converts monthly salary to annual salary by multiplying it by 12.

#### 2. `TCS` Class (Inherits from `Employee`):
- **Additional Attributes**: `location`, `dob`
- **Methods**:
    - `update(Location, DOB)`: Updates `location` and `dob` attributes.

#### 3. `HCL` Class (Inherits from `Employee`):
- **Additional Attributes**: `gender`, `blood_group`, `doj` (date of joining)
- **Methods**:
    - `update(Gender, Blood_Group, DOJ)`: Updates `gender`, `blood_group`, and `doj` attributes.

#### 4. `ZOHO` Class (Inherits from `Employee`):
- **Additional Attributes**: `experience`, `mobile`, `address`, `aadhar`
- **Methods**:
    - `update(Experience, Mobile, Address, Aadhar)`: Updates `experience`, `mobile`, `address`, and `aadhar` attributes.

### Object Instantiation and Method Calls:
1. Three employee objects are created: `Employee1` (TCS employee), `Employee2` (HCL employee), and `Employee3` (ZOHO employee).

2. Various methods are called on these objects:
    - `sal_with_flt()`: Formats salary for TCS employee.
    - `update()`: Updates location and DOB for TCS employee, gender, blood group, and DOJ for HCL employee, and experience, mobile, address, and Aadhar for ZOHO employee.
    - `name_split()`: Splits the name into first and last names for HCL employee.
    - `sal_with_pf_details()`: Reduces salary by 10% for HCL employee.
    - `Anual_Sal()`: Converts monthly salary to annual salary for ZOHO employee.

3. Finally, the `show()` method is called for each object, displaying the employee details with the modifications made through the `update()` method calls.

Please note that there are some issues in the original code that have been fixed in the corrected version provided earlier. The program demonstrates inheritance, object-oriented principles, and method calls on class objects.
