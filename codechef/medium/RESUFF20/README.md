# RESUFF20

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Assign Grades Based on Marks

Write a Program to Calculate the Grade Based on Marks This program prompts the user to enter their  **marks**  and uses a  **ternary operator**  to assign the corresponding grade based on the input. The grade will be one of  **"A+", "A", "B", "C", or "Fail"**, depending on the mark range.

 **Input:** 
A single integer representing the marks obtained by the student.

 **Condition:** 

- If the marks are 90 or above, assign grade "A+".
- If the marks are between 80 and 89, assign grade "A".
- If the marks are between 70 and 79, assign grade "B".
- If the marks are between 60 and 69, assign grade "C".
- If the marks are below 60, assign grade "Fail".

Run the program, enter different marks, and check the output for the corresponding grade!

### Sample 1:
Input
Output

```
85
```

```
The grade is: A

```

### Sample 2:
Input
Output

```
72
```

```
The grade is: B

```

## Solution

**Language:** Java  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T13:48:45.062Z  

```java
import java.util.Scanner; // Import Scanner class for taking input from the user

class Codechef {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in); // Create a Scanner object for user input

        // Read the marks input from the user
        int marks = scanner.nextInt(); 
        String grade="";
        if(marks>=90){
            grade="A+";
        }else if (marks>=80 && marks<90){
            grade="A";
        }else if(marks>=70 && marks<80){
            grade="B";
        }else if(marks>=60 && marks<70){
            grade="C";
        }else if(marks<60){
            grade="Fail";
        }
        System.out.println("The grade is: " +grade);

        scanner.close(); // Close the Scanner object to free up resources
    }
}

```

---

[View on CodeChef](https://www.codechef.com/problems/RESUFF20)