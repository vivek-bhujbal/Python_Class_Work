def total_cost(base_cost,tax_rate,tip_percentage):
    tax_amt = base_cost * tax_rate / 100

    tip_amt = base_cost * tip_percentage / 100

    total_cost = base_cost + tax_amt + tip_amt

    return total_cost


base_cost=int(input("Enter the Cost : "))
tax_rate=int(input("Enter Tax Rate : "))
tip_percentage=int(input("Enter Percentage : "))


total_cal_cost=total_cost(base_cost,tax_rate,tip_percentage)

print("Total Cost is : ",total_cal_cost)
