print("Grade Classification Sysytem")
print()

# Get input from student
gpa = input("Enter your GPA: ")

# Convert the input to a float
try:
    gpa = float(gpa)
    
    if gpa < 0 or gpa > 4:
        print("Error!: GPA must be between 0 and 4.00")
        
    elif gpa >= 3.5:
        print("GPA: {:.2f}".format(gpa))
        print("First Class Honours")
        
    elif gpa >= 3.0:
        print("GPA: {:.2f}".format(gpa))
        print("Second Class Honours (Upper Division)")
        
    elif gpa >= 2.0:
        print("GPA: {:.2f}".format(gpa))
        print("Second Class Honours (Lower Division)")
        
    elif gpa >= 1.0:
        print("GPA: {:.2f}".format(gpa))
        print("Third Class Honours")
    
    else:
        print("GPA: {:.2f}".format(gpa))
        print("Failed no Hours classification")
        
except:
    print("Error: please enter a valid GPA number")
    

        
    
    