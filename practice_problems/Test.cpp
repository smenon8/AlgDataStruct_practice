#include<iostream>

using namespace std;
int addAnArray(int a[])
{
	int varSum = 0;
	for(int i = 0; i < 10; i++)
	{
		varSum = varSum + a[i];
	}

	return varSum;
}

int main()
{
	int arr[10] ; 				        // An integer array that can hold 10 numbers
	int sum = 0;						// A variable sum to hold the sum of the array
	for(int i = 0; i < 10; i++ )        // A for loop that fills in the array with numbers 1..10
	{
		arr[i] = i ;
	}

	sum = addAnArray(arr);

	cout << "Sum = " << sum << endl;
}