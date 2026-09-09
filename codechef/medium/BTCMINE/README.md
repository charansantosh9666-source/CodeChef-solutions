# BTCMINE

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Coin Mining

Chef has decided to try and obtain a bit of side income by mining cryptocurrency.

Initially, Chef has $0$ GPUs.

At the beginning of each day, Chef can buy  **at most one**  GPU, for a cost of $X$ coins.
At the end of each day, if Chef has $K$ GPUs currently, they will mine a total of $Y\cdot K^2$ coins worth of currency on that day.

Chef's  *profit*  equals the total number of coins earned from mining so far, minus the total cost spent on GPUs so far.

If Chef chooses his actions optimally, find the minimum number of days needed till his profit becomes  **strictly positive**.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input, containing two space-separated integers $X$ and $Y$.
### Output Format

For each test case, output on a new line the minimum number of days needed for Chef to turn a profit.

### Constraints
- $1 \leq T \leq 100$
- $1 \le X, Y \le 200$
### Sample 1:
Input
Output

```
3
8 3
10 5
11 1

```

```
3
2
5

```

### Explanation:

 **Test case $1$:**  One optimal solution is as follows:

- Day $1$: Buy a GPU, paying $X=8$ coins. At the end of the day, we have $K = 1$ GPU so receive $Y\cdot K^2 = 3\cdot 1^2 = 3$ coins.
- Day $2$: Don't buy a GPU. At the end of the day, receive $3$ coins again since we still have only one GPU.
- Day $3$: Buy a GPU, paying $8$ coins. At the end of the day, we have $K = 2$ GPUs so receive $Y\cdot K^2 = 3\cdot 2^2 = 12$ coins.

At the end of the third day, we have received $3+3+12 = 18$ coins, and paid $8+8 = 16$ coins. Thus, we've made an overall profit of $2$ coins and so we're done.

It can be verified that there's no way to make a positive profit by the end of the second day, and so $3$ is optimal.

 **Test case $2$:**  Buy a GPU on both days $1$ and $2$, paying $10+10 = 20$ coins and obtaining a total revenue of $5\cdot 1^2 + 5\cdot 2^2 = 25$ coins by the end of the second day, thus leading to a profit of $5$ coins in total which is positive.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-09T15:11:19.655Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;
void solve() {
    long long X, Y;
    cin >> X >> Y;

    long long max_days = 205; 
    vector<long long> dp(max_days + 1, -1e18);
    dp[0] = 0;

    for (int day = 1; day <= max_days; ++day) {
        vector<long long> next_dp(max_days + 1, -1e18);
        for (int gpus = 0; gpus <= day; ++gpus) {
            if (dp[gpus] < -1e17) continue;

            long long p1 = dp[gpus] + Y * gpus * gpus;
            next_dp[gpus] = max(next_dp[gpus], p1);

            long long p2 = dp[gpus] - X + Y * (gpus + 1) * (gpus + 1);
            next_dp[gpus + 1] = max(next_dp[gpus + 1], p2);
        }
        dp = move(next_dp);

        for (int gpus = 0; gpus <= day; ++gpus) {
            if (dp[gpus] > 0) {
                cout << day << "\n";
                return;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/BTCMINE)