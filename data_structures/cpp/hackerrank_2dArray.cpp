// HACKER RANK - https://www.hackerrank.com/challenges/2d-array/problem

#include <bits/stdc++.h>

using namespace std;
int getTopWindow(vector<vector<int>> & arr, const size_t i, const size_t j) {
    return arr[i][j] + arr[i][j+1] + arr[i][j+2] ;
}

int getMidWindow(vector<vector<int>> & arr, const size_t i, const size_t j) {
    return arr[i+1][j+1]  ;
}

int getBottomWindow(vector<vector<int>> & arr, const size_t i, const size_t j) {
    return getTopWindow(arr, i+2, j) ;
}
// Complete the hourglassSum function below.
int hourglassSum(vector<vector<int>> arr) {

    vector<int> sums;
    for (size_t i = 0; i < 4; ++i) {
        for (size_t j = 0; j < 4; ++j) {
            sums.push_back(getTopWindow(arr, i, j) + 
                          getMidWindow(arr, i, j) + 
                          getBottomWindow(arr, i, j));
        }
    }
    
    // find max
    int max = INT_MIN;
    for (size_t it = 0; it != sums.size(); ++it) {
        if (sums[it] > max)
            max = sums[it];
    }
    
    return max;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    vector<vector<int>> arr(6);
    for (int i = 0; i < 6; i++) {
        arr[i].resize(6);

        for (int j = 0; j < 6; j++) {
            cin >> arr[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int result = hourglassSum(arr);

    fout << result << "\n";

    fout.close();

    return 0;
}

