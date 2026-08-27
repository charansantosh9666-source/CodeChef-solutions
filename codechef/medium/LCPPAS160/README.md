# LCPPAS160

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program to accept as input the length and all the elements of an array

You need to output the difference between the sum of all the even index elements and the sum of the odd index elements.

### Sample 1:
Input
Output

```
5
1 2 3 4 5
```

```
3
```

### Explanation:

1 + 3 + 5 - (2 + 4) = 3

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-27T16:40:42.151Z  

```c_cpp
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n;
	cin>>n;
	int arr[n];
	for(int i=0;i<n;i++){
	    cin>>arr[i];
	}
	int a=0,b=0;
	for(int j=0;j<n;j++){
	    if(arr[j]%2!=0){
	        a+=arr[j];
	    }else{
	        b+=arr[j];
	    }
	}
	cout<<a-b;
	return 0;
}

```

---

[View on CodeChef](https://www.codechef.com/problems/LCPPAS160)