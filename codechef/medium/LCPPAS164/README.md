# LCPPAS164

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer  **N**, print the number of elements between $1$ and  **N**  that are  **not divisible**  by $2$, $3$, or $5$.

 **Input Format** 
The first line contains a single integer N, entered by the user.

 **Output Format** 
Print a single integer - the count of numbers between 1 and N (inclusive) that are not divisible by 2, 3, or 5.

### Sample 1:
Input
Output

```
10
```

```
2
```

### Explanation:

1 and 7 are not divisible by 2, 3 or 5

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-27T16:54:06.778Z  

```c_cpp
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n;
	cin>>n;
	int c=0;
	for(int i=1;i<=n;i++){
	    if(i%2!=0 && i%3!=0 || i%5!=0){
	        c++;
	    }
	}
	cout<<c;
	return 0;
}

```

---

[View on CodeChef](https://www.codechef.com/problems/LCPPAS164)