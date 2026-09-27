# Given dictionary
student_grades = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 65, "Eva": 88, "John": 45}
a=input()
# Complete the code 
if a in student_grades:
    ans=student_grades[a]
    print(ans)
else:
    print("Not Found")
