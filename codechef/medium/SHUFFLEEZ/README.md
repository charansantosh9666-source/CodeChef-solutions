# SHUFFLEEZ

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Shuffle (Easy)

 **This is the easy version of the problem. Here, the final permutation $Q$ is always the identity permutation.** 

For a permutation $P$ of the integers $[1, N]$ and an integer $K$, define $f(P, K)$ as the permutation formed at the end of the following process:

- For each $i = 1, 2, \ldots, N - K + 1$ (in this order), sort the subarray $P[i, i + K - 1]$.

For example, $f([3, 2, 1], 2) = [2, 1, 3]$. First $P[1, 2]$ gets sorted, so $P = [2, 3, 1]$ and then $P[2, 3]$ gets sorted, so $P = [2, 1, 3]$.

You are given integers $N$ and $K$, and a permutation $Q$. Here, $Q$ is always identity permutation, i.e. $Q_i = i$ for all $i$.

Count the number of permutations $P$ such that $f(P, K) = Q$ modulo $998244353$.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains $2$ integers - $N$ and $K$. The second line contains $N$ integers - $Q_1, Q_2, \ldots, Q_N$.
### Output Format

For each test case, output on a new line the number of permutations $P$ modulo $998244353$.

### Constraints
- $1 \le T \le 10^4$
- $2 \le K \le N \le 2 \cdot 10^5$
- $Q_i = i$
- The sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.
### Sample 1:
Input
Output

```
3
3 2
1 2 3
3 3
1 2 3
5 3
1 2 3 4 5

```

```
4
6
54
```

### Explanation:

 **Test Case 1:**  The valid permutations $P$ are $[1, 2, 3]$, $[2, 1, 3]$, $[1, 3, 2]$ and $[3, 1, 2]$.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T15:47:17.858Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;


const int MOD = 998244353;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

void solve() {
    long long n, k;
    cin >> n >> k;
    
    vector<int> q(n);
    for (int i = 0; i < n; i++) {
        cin >> q[i];
    }
    
    long long fact_k = 1;
    for (int i = 1; i <= k; i++) {
        fact_k = (fact_k * i) % MOD;
    }
    
    long long pow_k = power(k, n - k);
    
    long long ans = (fact_k * pow_k) % MOD;
    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/SHUFFLEEZ)