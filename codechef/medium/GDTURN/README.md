# GDTURN

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-27T17:16:01.726Z  

```c_cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Update your code here.
    int t;
    cin>>t;
    while(t--){
        int n,sum=0;
        cin>>n;
        int arr[n];
        for(int i=0;i<n;i++){
            cin>>arr[i];
            if(arr[i]%3==0){
                sum+=arr[i];
            }
        }
        cout<<sum<<endl;
    }
    return 0;
}

```

---

[View on CodeChef](https://www.codechef.com/problems/GDTURN)