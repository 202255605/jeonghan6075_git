#include <stdio.h> 

int main(void)
{
	int a[10]={11,22,33,44,55};
	int i, j, n=5;

	scanf("%d", &j);
	// Enter your code here
 	if(j>=5) j=n;
	if(j<1) j=n;
	
	int b[5],number,number_2,account;
	
	for(number=0;number<j-1;number++){
		b[number]=a[number];//0-(j-2) 즉 개수는 j-1개
	}

	for(number_2=j;number_2<=4;number_2++){
		b[number_2-1]=a[number_2];//인자가 j-1부터 다 들어온다.
	}

	for(account=j;account<=4;account++){
		a[account-1]=b[account-1];
	}
	
	n=4;

	for(i=0;i<n;++i) 
		printf("%d ", a[i]);
	printf("\n");
	
	return 0;
}