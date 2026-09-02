# Given dictionary
student_grades = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 65, "Eva": 88, "John": 45}

# Complete the code 
a=input()
c=0
for i in student_grades:
    if(a==i):
        print(student_grades[i])
        c=c+1
if(c==0):
    print("Not Found")