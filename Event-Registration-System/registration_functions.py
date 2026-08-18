registered_talents = []

def validate_age(age_input):
    try:
        age = int(age_input)
        if age <= 0:
            print("\nError: Age must be a positive number.")
            return -1
        return age
    except ValueError:
        print("\nError: Please enter a valid number for age.")
        return -1

def add_talent(name, age, category):
    talent_data = {
        "name": name,
        "age": age,
        "category": category
    }
    registered_talents.append(talent_data)
    print(f"\nSuccess: '{name}' has been registered successfully for the {category} category!")

def display_all_talents():
    if not registered_talents:
        print("\nNo talents registered yet. The list is empty.")
        return
    
    print("\n--- Registered Talents ---")
    for index, talent in enumerate(registered_talents, start=1):
        print(f"{index}. Name: {talent['name']} | Age: {talent['age']} | Category: {talent['category']}")
    print("--------------------------")