#include <iostream>
#include <limits.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
	cin.tie(nullptr);

    // freopen("in.txt"r, "r", stdin);

    int t; cin >> t;
    while (t--) {
        // cout << "Runnning tc" << t;
        int n, k; cin >> n >> k;
        bool steps[n];
        string s; cin >> s;
        for (int i = 0; i < n; ++i) {
            steps[i] = s[i] == '0';
        }
        int i = 0;
        int jumps = 0;
        bool unsolvable = 0;
        while (i < n-1) {
            ++jumps;
            int max_jump = min(n-1, i+k);
            int optimal_jump = -1;
            for (int next = max_jump; next >= i+1; --next)
                if (steps[next]) {
                    // jump here
                    optimal_jump = next;
                    break;
                }
            if (optimal_jump == -1) { // cannot complete
                unsolvable = 1;
                break;
            }
            i = optimal_jump;
        }
        if (unsolvable) {
            cout << "-1\n";
            continue;
        }
        cout << jumps << endl;

    }
}

        // int dp[n]; // How many steps it takes to get to each step
        // // Initialize dp
        // for (int i = 1; i < n; ++i) dp[i] = -1; // -1 indicates we cannot reach this step
        // // We can step on stair 0
        // dp[0] = 0;

        // for (int i = 0; i < n; ++i) {
        //     if (!steps[i]) continue; // we cannot go to any step from this
        //     // How many steps forward we can go
        //     for (int j = 1; j < k; ++j) {
        //         steps[j] = INT_MAX;
        //     }
        // }