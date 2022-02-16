## 跳蚱蜢

如图 p1.png 所示： 有9只盘子，排成1个圆圈。

其中8只盘子内装着8只蚱蜢，有一个是空盘。

我们把这些蚱蜢顺时针编号为 1~8。

每只蚱蜢都可以跳到相邻的空盘中，也可以再用点力，越过一个相邻的蚱蜢跳到空盘中。

请你计算一下，如果要使得蚱蜢们的队形改为按照逆时针排列，并且保持空盘的位置不变（也就是1-8换位，2-7换位,...），至少要经过多少次跳跃？

注意：要求提交的是一个整数，请不要填写任何多余内容或说明文字。

## Ideas

首先我们是要搜索一种方案，来达到蚱蜢位置变换的目的，所以确定这道题是一道搜索问题。

其次，题目要求的是至少要经过多少次跳跃，所以是一个最优问题，应该用广度优先搜索BFS。

之后我们要把题目中的场景抽象为计算机表达形式，虽然是9个盘子排成了1一个圆圈，其中有8个盘子里面有蚱蜢，所以我们可以用`012345678`来表示初始状态，其中0就是空盘子。

我们的目标是按照规则进行跳蚱蜢，让蚱蜢的队形改为逆时针排列，即目标状态为`087654321`。

对于这种圆形的操作，我们可以通过取余来实现，比如8号盘子的蚱蜢要往前跳一位，就是(8 + 1) % 9，即跳到了0位置。

最后就是实现BFS的过程了，直接套模板，然后需要修改的是状态转移的逻辑。

题目中说的是”每只蚱蜢都可以跳到相邻的空盘中， 也可以再用点力，越过一个相邻的蚱蜢跳到空盘中。“

也就是说，首先我们需要找到空盘子的位置，然后空盘子前后两个盘子的蚱蜢可以跳到空盘子上，空盘子前面第二个盘子和后面第二个盘子的蚱蜢也可以跳到空盘子上，对应到计算机表示其实就是swap操作。

然后就可以开始写代码啦。

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

		x = item.index('0')  # 空盘位置
		item = list(item)
		for dx in [2, 1, -1, -2]:
			nx = (x + dx) % 9
			item[x], item[nx] = item[nx], item[x]
			new = ''.join(item)
			if new not in states:
				queue.append((''.join(item), cnt + 1))
			item[x], item[nx] = item[nx], item[x]   # 跳完之后要恢复之前的状态再做尝试


if __name__ == '__main__':
	source = "012345678"
	target = "087654321"
	states = set()

	bfs()
```