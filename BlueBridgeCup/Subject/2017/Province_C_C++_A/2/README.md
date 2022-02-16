## ������

��ͼ p1.png ��ʾ�� ��9ֻ���ӣ��ų�1��ԲȦ��

����8ֻ������װ��8ֻ���죬��һ���ǿ��̡�

���ǰ���Щ����˳ʱ����Ϊ 1~8��

ÿֻ���춼�����������ڵĿ����У�Ҳ�������õ�����Խ��һ�����ڵ��������������С�

�������һ�£����Ҫʹ�������ǵĶ��θ�Ϊ������ʱ�����У����ұ��ֿ��̵�λ�ò��䣨Ҳ����1-8��λ��2-7��λ,...��������Ҫ�������ٴ���Ծ��

ע�⣺Ҫ���ύ����һ���������벻Ҫ��д�κζ������ݻ�˵�����֡�

## Ideas

����������Ҫ����һ�ַ��������ﵽ����λ�ñ任��Ŀ�ģ�����ȷ���������һ���������⡣

��Σ���ĿҪ���������Ҫ�������ٴ���Ծ��������һ���������⣬Ӧ���ù����������BFS��

֮������Ҫ����Ŀ�еĳ�������Ϊ����������ʽ����Ȼ��9�������ų���1һ��ԲȦ��������8���������������죬�������ǿ�����`012345678`����ʾ��ʼ״̬������0���ǿ����ӡ�

���ǵ�Ŀ���ǰ��չ�����������죬������Ķ��θ�Ϊ��ʱ�����У���Ŀ��״̬Ϊ`087654321`��

��������Բ�εĲ��������ǿ���ͨ��ȡ����ʵ�֣�����8�����ӵ�����Ҫ��ǰ��һλ������(8 + 1) % 9����������0λ�á�

������ʵ��BFS�Ĺ����ˣ�ֱ����ģ�壬Ȼ����Ҫ�޸ĵ���״̬ת�Ƶ��߼���

��Ŀ��˵���ǡ�ÿֻ���춼�����������ڵĿ����У� Ҳ�������õ�����Խ��һ�����ڵ��������������С���

Ҳ����˵������������Ҫ�ҵ������ӵ�λ�ã�Ȼ�������ǰ���������ӵ�������������������ϣ�������ǰ��ڶ������Ӻͺ���ڶ������ӵ�����Ҳ���������������ϣ���Ӧ���������ʾ��ʵ����swap������

Ȼ��Ϳ��Կ�ʼд��������

## Code

### C++

```cpp
#include <iostream>
#include <cstring>
#include <string>
#include <cstdlib>
#include <queue>
#include <set>
using namespace std;
char *start="012345678";
char *target="087654321";
struct StateAndLevel
{
	char *state;
	int level;
	int pos0;

	StateAndLevel(char *_state,int _level,int _pos0):state(_state),level(_level),pos0(_pos0){}
};
struct cmp
{
	bool operator()(char *a,char *b)
	{
		return strcmp(a,b)<0;
	}
};
void swap(char *s, int a, int b)
{
    char t = s[a];
    s[a] = s[b];
    s[b] = t;
}
queue<StateAndLevel> q;
set<char *,cmp> allState;
void addNei(char *state,int pos,int newPos,int le)
{
	char *new_state=(char*)malloc(9* sizeof(char));
	strcpy(new_state,state);
	swap(new_state,pos,newPos);
	if(allState.find(new_state)==allState.end())
	{
		allState.insert(new_state);
		q.push(StateAndLevel(new_state,le+1,newPos));
	}
}
int main()
{
	q.push(StateAndLevel(start,0,0));
	allState.insert(start);

	while(!q.empty())
	{
		StateAndLevel sal=q.front();
		char *state=sal.state;
		int le=sal.level,pos0=sal.pos0,new_pos;
		if(strcmp(state,target)==0)
		{
			cout << le << endl;
			return 0;
		}
		new_pos=(pos0-1+9)%9;
		addNei(state,pos0,new_pos,le);
		new_pos=(pos0-2+9)%9;
		addNei(state,pos0,new_pos,le);
		new_pos=(pos0+1+9)%9;
		addNei(state,pos0,new_pos,le);
		new_pos=(pos0+2+9)%9;
		addNei(state,pos0,new_pos,le);
		q.pop();
	}
	return 0;
}
```

### Python

```python
from collections import deque


def bfs():
	queue = deque()
	queue.append((source, 0))
	while queue:
		front = queue.popleft()
		item, cnt = front

		if item == target:
			print(cnt)
			return

		if item in states:
			continue
		states.add(item)

		x = item.index('0')  # ����λ��
		item = list(item)
		for dx in [2, 1, -1, -2]:
			nx = (x + dx) % 9
			item[x], item[nx] = item[nx], item[x]
			new = ''.join(item)
			if new not in states:
				queue.append((''.join(item), cnt + 1))
			item[x], item[nx] = item[nx], item[x]   # ����֮��Ҫ�ָ�֮ǰ��״̬��������


if __name__ == '__main__':
	source = "012345678"
	target = "087654321"
	states = set()

	bfs()
```