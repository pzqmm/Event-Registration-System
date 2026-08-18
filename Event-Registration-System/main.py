import registration_functions as rf

def main():
    print("==================================================")
    print(" Welcome to the Casting Call Registration System  ")
    print("==================================================")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Register a new talent")
        print("2. View all registered talents")
        print("3. Exit System")
        
        choice = input("Please select an option (1, 2, or 3): ")
        
        if choice == '1':
            print("\n-- New Registration --")
            name = input("Enter talent's full name: ")
            
            while True:
                age_input = input("Enter talent's age: ")
                valid_age = rf.validate_age(age_input)
                if valid_age != -1:
                    break
                    
            category = input("Enter talent category: ")
            
            rf.add_talent(name, valid_age, category)
            
        elif choice == '2':
            rf.display_all_talents()
            
        elif choice == '3':
            print("\nThank you for using the Registration System. Goodbye!")
            break
            
        else:
            print("\nInvalid choice! Please only select 1, 2, or 3.")

if __name__ == "__main__":
    main()