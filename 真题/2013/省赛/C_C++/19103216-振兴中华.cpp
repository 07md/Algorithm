#include<stdio.h>
int count=0;
void road(int row,int line,int arr[][5])
{
	if(arr[row][line]==7)//��0��ʼ����7��Ϊһ������·�� 
		count++;
	
	if(line+1<5 && arr[row][line+1]==arr[row][line]+1)//������ 
		road(row,line+1,arr);
		
	if(row+1<4 && arr[row+1][line]==arr[row][line]+1)//������ 
		road(row+1,line,arr);
}
int main()
{
	int arr[4][5]={
	            {0,1,2,3,4},
	            {1,2,3,4,5},
			    {2,3,4,5,6},
			    {3,4,5,6,7}};
	road(0,0,arr);
	printf("%d",count);
	return 0;			   
}
