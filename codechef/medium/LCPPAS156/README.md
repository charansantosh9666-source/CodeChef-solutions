# LCPPAS156

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program to input two student's names and percentages and print the name of the student with the higher percentage. In case they score equal percentages, print ' **equal** '.

### Input Format
- The first line of input will contain two strings: the name of the first student and the name of the second student.
- The second line of input will contain two percentages: the percentage of the first student and the percentage of the second student.
### Sample 1:
Input
Output

```
Amit Swarup
95 92
```

```
Amit
```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-27T16:36:12.162Z  

```c_cpp
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	string s1,s2;
	int a,b;
	cin>>s1>>s2;
	cin>>a>>b;
	if(a>b){
	    cout<<s1;
	}else if(b>a){
	    cout<<s2;
	}else{
	    cout<<"equal";
	}
	return 0;
}

```

---

[View on CodeChef](https://www.codechef.com/problems/LCPPAS156)