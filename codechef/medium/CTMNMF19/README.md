# CTMNMF19

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Print Even Numbers Using a While Loop

A Java program that prints all  **even numbers**  from  **2**  up to a given number (**n**) using a  **while loop**.

 **Input:** 
Take input of n from user.

### Sample 1:
Input
Output

```
10
```

```
Even numbers from 2 to 10:
2
4
6
8
10

```

### Sample 2:
Input
Output

```
2
```

```
Even numbers from 2 to 2:
2
```

### Sample 3:
Input
Output

```
1
```

```
 
```

## Solution

**Language:** Java  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-03T01:38:37.896Z  

```java
import java.util.*;
class Codechef {
    public static void main(String[] args) {
        Scanner s= new Scanner(System.in);
        //Take input of n from user
        int n= s.nextInt();
        
        int number = 2; // Starting with the first even number
        
        System.out.println("Even numbers from 2 to " + n + ":");
        
        while (number <= n) {  // Continue loop until number is less than or equal to n
            if(number%2==0){
                System.out.println(number);
                
            }
            number++;
        }
    }
}


```

---

[View on CodeChef](https://www.codechef.com/problems/CTMNMF19)