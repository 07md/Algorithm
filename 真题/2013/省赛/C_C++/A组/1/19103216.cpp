/*��˹�����ڣ�1777��4��30�ա�
�ڸ�˹���ֵ�һ����Ҫ������ռ��ϱ�ע�ţ�5343��
��˿���������ǣ�1791��12��15�ա�
��˹��ò�ʿѧλ�������ռ��ϱ��ţ�8113   
���������˹��ò�ʿѧλ�������ա�*/

#include <stdio.h>

int main()
{
	int year,year_plus,month=0,day;
//4��30��Ϊ�����120�� 
	int date=8113+120-1;
	
	year_plus = date/365;
	year = 1777 + year_plus;
	for(int i=1777;i<year;i++)
	{
		if(i%400==0 || (i%100!=0&&i%4==0))
		{
			date--;
		}
	}
	int sum = date - 365*year_plus;
	
	int sum_day=0;
	int arr[12]={0,31,28,31,30,31,30,31,31,30,31,30};
	for(int i=0;i<12;i++)
	{		
		sum_day += arr[i];
		month++;
		if(sum_day+arr[i+1]>=sum)
			break;
	}
	if( (year%400==0 || (year%100!=0&&year%4==0))&&month>2 )
		sum_day++;
		
	day = sum - sum_day;
	
	if(day==0)
		day=31;
		
	if(month>9&&day>9)
		printf("%d-%d-%d",year,month,day);
	if(month>9&&day<10)
		printf("%d-%d-0%d",year,month,day);	
	if(month<10&&day>10)
		printf("%d-0%d-%d",year,month,day);
	if(month<10&&day<10)
		printf("%d-0%d-0%d",year,month,day);
	return 0;
}
