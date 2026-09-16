# FARSWAP

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Far Swapping (Ver 2)

You are given a permutation $P$ of the integers $[1, N]$. You can use the following operation as many times as you want:

- Choose an index $i$ ($1 \le i < N$) such that $|P_i - P_{i + 1}| > 1$
- Swap $P_i$ and $P_{i + 1}$.

Count the number of permutations that are reachable using the above operation multiple times (possibly $0$). Since the answer may be large, find it modulo $998244353$.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains a single integer $N$. The second line contains $N$ integers - $P_1, P_2, \ldots, P_N$.
### Output Format

For each test case, output on a new line the number of reachable permutations modulo $998244353$.

### Constraints
- $1 \le T \le 10^4$
- $2 \le N \le 3000$
- $1 \le P_i \le N$
- $P_i \ne P_j$ for all $i \ne j$
- The sum of $N^2$ over all test cases does not exceed $3000^2$
### Sample 1:
Input
Output

```
3
3
1 3 2
3
3 2 1
5
5 2 3 1 4

```

```
2
1
11
```

### Explanation:

 **Test Case 1:**  $[1, 3, 2]$ and $[3, 1, 2]$ are reachable. The former is just the original permutation itself, and the latter can be reached by swapping $P_1$ and $P_2$. Note that $2 = P_3$ cannot be swapped with anybody due to the absolute difference $> 1$ condition.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-16T15:18:03.833Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;
const long long MOD = 998244353;

int main() {
	// your code goes here
	ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;

        vector<int> P(N + 1), pos(N + 1);

        for (int i = 1; i <= N; i++) {
            cin >> P[i];
            pos[P[i]] = i;
        }
        vector<long long> dp(N + 1), ndp(N + 1);
        dp[1] = 1;

        for (int len = 2; len <= N; len++) {
            vector<long long> pref(len, 0);
            for (int j = 1; j <= len - 1; j++) {
                pref[j] = (pref[j - 1] + dp[j]) % MOD;
            }

            fill(ndp.begin(), ndp.end(), 0);
            if (pos[len - 1] < pos[len]) {
                for (int j = 1; j <= len; j++) {
                    ndp[j] = pref[j - 1];
                }
            } else {
                long long total = pref[len - 1];

                for (int j = 1; j <= len; j++) {
                    ndp[j] = (total - pref[j - 1] + MOD) % MOD;
                }
            }

            dp.swap(ndp);
        }

        long long ans = 0;
        for (int j = 1; j <= N; j++) {
            ans = (ans + dp[j]) % MOD;
        }

        cout << ans << '\n';
    }

    return 0;

}

```

---

[View on CodeChef](https://www.codechef.com/problems/FARSWAP)