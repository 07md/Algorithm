#include <iostream>
using namespace std;

int dire[4][2]={{-1,0},{1,0},{0,-1},{0,1}};
int visited[7][7],ans;
void dfs(int x,int y)
{
	if(x==0||y==0||x==6||y==6)
	{
		ans++;
		return;
	}
	visited[x][y]=1;
	visited[6-x][6-y]=1;
	for(int k=0;k<4;k++)
	{
		int nx=x+dire[k][0];
		int ny=y+dire[k][1];
		if(nx<0||nx>6||ny<0||ny>6) continue;
		if(!visited[nx][ny]) dfs(nx,ny);
	}
	visited[x][y]=0;
	visited[6-x][6-y]=0;
}
int main()
{
	dfs(3,3);
	cout<<ans/4<<endl;
	return 0;
}
