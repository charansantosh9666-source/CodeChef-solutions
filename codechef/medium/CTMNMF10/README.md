# CTMNMF10

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Sum of Digits Calculator

A banking application ensures data integrity by verifying the sum of digits in an account number. This helps in detecting data entry errors when customers register their account details. The system extracts and sums all digits in the account number and verifies it against the expected digit sum.

 **Steps to Complete:** 

- Read an integer from the user.
- Initialize a sum variable to store the total sum of digits.
- Use a while loop to extract each digit using the modulus operator (%).
- Add the extracted digit to the sum.
- Print the final sum of the digits until number!=0.
### Sample 1:
Input
Output

```
456
```

```
Sum of digits: 15
```

### Sample 2:
Input
Output

```
1023
```

```
Sum of digits: 6
```

## Solution

**Language:** Java  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T03:04:46.617Z  

```java
import java.util.Scanner;  

class Codechef {  
    public static void main(String[] args) {
        
        // Create a Scanner object to read input from the user
        Scanner scanner = new Scanner(System.in);  
        
        // Read an integer input from the user
        int number = scanner.nextInt();  
        int sum=0;
        while(number>0){
            sum+=number%10;
            number/=10;
        }

        // Print the result, which is the sum of the digits
        System.out.println("Sum of digits: " + sum);
    }  
}
```

---

[View on CodeChef](https://www.codechef.com/problems/CTMNMF10)