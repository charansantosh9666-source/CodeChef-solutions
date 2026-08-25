# RESUFF26

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Java  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T13:57:16.074Z  

```java
import java.util.Scanner;

class Codechef {
    public static void main(String[] args) {
        
        Scanner sc= new Scanner(System.in);
        int age = sc.nextInt(); // User's age
        boolean hasMembershipCard = sc.nextBoolean(); 
        boolean isAccompaniedByMember = sc.nextBoolean(); 
        boolean isBanned = sc.nextBoolean();        
        if (isBanned) {
            System.out.println("Not eligible for gym entry due to ban.");
        } 
        else if (age >= 18 && hasMembershipCard) {
            System.out.println("Eligible for gym entry with a membership card.");
        } 
        else if (age >= 18 && isAccompaniedByMember) {
            System.out.println("Eligible for gym entry when accompanied by a member.");
        } 
        else {
            System.out.println("Not eligible for gym entry.");
        }
    }
}

```

---

[View on CodeChef](https://www.codechef.com/problems/RESUFF26)