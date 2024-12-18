def birthday():
    import datetime
    
    year = int(input("Enter Birth year (e.g., 2004): "))
    month = int(input("Enter Birth month (1-12): "))
    day = int(input("Enter Birth day (1-31): "))
    
    # This is Today's date
    today = datetime.datetime.now().date()
    
    # Create a date object for the date of birth
    dob = datetime.date(year, month, day)
    
    # Now we will calculate the age
    age = int((today - dob).days / 365)
    
    # Print the result
    print(f"You are {age} years old.")

# Call the birthday function
birthday()

