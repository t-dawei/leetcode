#include<iostream>
const int MAX = 101;
int matrix[MAX][MAX];
int DP[MAX][MAX];
using namespace std;
int main()
{
	int n, i, j, Max, maxn, sum;
	while (cin >> n)
	{
		for (i = 1; i <= n; i++)
		{
			for (j = 1; j <= n; j++)
			{
				cin >> matrix[i][j];
			}
		}
		for (int k = 0; k < MAX; k++)
			for (int h = 0; h < MAX; h++)
				DP[k][h] = 0;
		//memset(DP, 0, sizeof(DP));
		for (i = 1; i <= n; i++)
		{
			for (j = 1; j <= n; j++)
			{
				DP[j][i] = DP[j][i - 1] + matrix[i][j];
			}
		}
		Max = 0;
		for (i = 1; i <= n; i++)
		{
			for (j = i; j <= n; j++)
			{
				maxn = 0;
				sum = 0;
				for (int k = 1; k <= n; k++)
				{
					sum += DP[k][j] - DP[k][i - 1];
					if (sum>0)
					{
						if (sum>maxn)
							maxn = sum;
					}
					else
						sum = 0;
				}
				if (maxn>Max)
					Max = maxn;
			}
		}
		cout << Max << endl;
	}
	return 0;
}