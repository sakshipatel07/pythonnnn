from datetime import datetime

def calculate_age():
    birth_date = input("Enter your birthdate (YYYY-MM-DD): ")

    try:
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
        today = datetime.today()
        
        # Calculate age
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        print(f"You are {age} years old.")
    except ValueError:
        print("Invalid format! Please enter the date in YYYY-MM-DD format.")

calculate_age()