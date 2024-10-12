basic_pay = float(input("Enter basic pay: "))
HRA = 0.10 * basic_pay
TA = 0.05 * basic_pay
total_salary = basic_pay + HRA + TA
print(f"The total salary is: {total_salary}")
