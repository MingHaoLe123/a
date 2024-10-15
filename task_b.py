try:
     grade = float(input("Enter a numerical grade between 0 and 100: "))

     if grade < 0 or grade > 100:
        print("Error: Grades must be between 0 and 100")
     else:
            if grade >= 80:
                 grade = 'A'
            elif grade >= 60:
                 grade = 'B'
            elif grade >= 50:
                 grade = 'C'
            elif grade >= 40:
                 grade = 'D'
            else:
                 grade = 'F'
             
            print(f"Your grade is:{grade}")

except ValueError:
    
    print("Error: Please enter a number")
