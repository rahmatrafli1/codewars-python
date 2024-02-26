def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth

    if age == 0:
        return "You were born this very year!"
    elif age < -1:
        return f"You will be born in {abs(age)} years."
    elif age == -1:
        return f"You will be born in {abs(age)} year."
    elif age == 1:
        return f"You are {age} year old."
    else:
        return f"You are {age} years old."