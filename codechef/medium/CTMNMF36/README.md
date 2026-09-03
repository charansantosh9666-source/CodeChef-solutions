# CTMNMF36

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Java  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-03T01:50:49.831Z  

```java
import java.util.Scanner;
class Codechef {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int a=s.nextInt();
        int i=1;
        while(i<=a){
            if(i%3==0 && i%5==0){
                System.out.println(i);
                
            }
            i++;
        }
        s.close();
    }
}
```

---

[View on CodeChef](https://www.codechef.com/problems/CTMNMF36)