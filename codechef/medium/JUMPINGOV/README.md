# JUMPINGOV

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Jumping Over

You are given a permutation $P$ of the integer $[1, N]$ and can perform the following operation:

- Choose an index $i$, and move it to the front or the back of the permutation (appropriately shifting the other indices).
- The cost of moving it to the front is $(i - 1)$, and the cost of moving it to the back is $(N - i)$, i.e. the cost is simply the number of elements it jumps over.

Find the minimum total cost of operations needed to sort the permutation $P$.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains a single integer $N$. The second line contains $N$ integers - $P_1, P_2, \ldots, P_N$.
### Output Format

For each test case, output on a new line the minimum cost.

### Constraints
- $1 \le T \le 10^4$
- $2 \le N \le 2 \cdot 10^5$
- $1 \le P_i \le N$
- $P_i \ne P_j$ for all $i \ne j$
- The sum of $N$ over all test cases does not exceed $2 \cdot 10^5$
### Sample 1:
Input
Output

```
4
2
2 1
4
4 2 3 1
3
1 2 3
6
2 4 1 6 5 3

```

```
1
5
0
10
```

### Explanation:

 **Test Case 1:**  You can choose the element $2$ at index $1$ and move it back, jumping over $1$ element. Then, the permutation is sorted, so the cost is only $1$.

 **Test Case 2:**  Move the value $4$ to the back, cost $3$, permutation is $[2, 3, 1, 4]$; and then move the value $1$ to the front, cost $2$. The total cost is $5$.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-16T15:20:38.483Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;

        vector<int> pos(N + 1);

        for (int i = 1; i <= N; ++i) {
            int x;
            cin >> x;
            pos[x] = i;
        }
        vector<ll> PF(N + 1, 0);

        for (int v = 1; v <= N; ++v) {
            PF[v] = PF[v - 1] + (pos[v] - 1LL);
        }
        vector<ll> SB(N + 2, 0);

        for (int v = N; v >= 1; --v) {
            SB[v] = SB[v + 1] + (N - pos[v]);
        }

        ll ans = LLONG_MAX;

        int a = 1;

        while (a <= N) {
            int b = a;

            while (b + 1 <= N && pos[b] < pos[b + 1]) {
                ++b;
            }
            ll bestLeft = LLONG_MAX;

            for (int r = a; r <= b; ++r) {
                bestLeft = min(bestLeft, PF[r - 1]);

                ans = min(ans, bestLeft + SB[r + 1]);
            }

            a = b + 1;
        }

        cout << ans << '\n';
    }

    return 0;
}

```

---

[View on CodeChef](https://www.codechef.com/problems/JUMPINGOV)