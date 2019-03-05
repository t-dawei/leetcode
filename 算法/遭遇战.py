#!/usr/bin/python
# -*- coding: utf-8 -*-

import collections

cnt = 0
n, s, e = map(int, input().split())


list_head = collections.defaultdict(int)


dict_d = {}
dict_f = {}
for i in range(s, e+2):
	dict_d[i] = float('inf')
	dict_f[i] = 0


list_q = []
dict_0 = {}
list_edge = []
list_edge.append(dict_0)

def addEdge(x, y, w):
	global cnt
	cnt += 1
	dict_ = {}
	dict_['to'] = y
	dict_['w'] = w
	dict_['next'] = list_head.get(x, 0)
	list_edge.append(dict_)
	list_head[x] = cnt

def spfa(s):
	list_q.append(s)
	dict_d[s] = 0
	dict_f[s] = 1
	while list_q:
		k = list_q.pop(0)
		dict_f[k] = 0

		i = list_head.get(k)
		while i:
			kk = list_edge[i]['to']
			if dict_d[kk] > dict_d[k] + list_edge[i]['w']:
				dict_d[kk] = dict_d[k] + list_edge[i]['w']	
				if dict_f[kk] == 0:
					dict_f[kk] = 1
					list_q.append(kk)
			i = list_edge[i]['next']

for i in range(1, n+1):
	si, ei, ci = map(int, input().split())
	if si <= e and ei >= s:
		addEdge(max(si, s),  min(ei + 1, e + 1), ci)

for i in range(s+1, e+2):
	addEdge(i, i-1, 0)

spfa(s)
if dict_d[e+1] != float('inf'):
	print(dict_d[e+1])
else:
	print('-1')


'''
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#define INF 0x7fffffff
#define SUP 0x80000000
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;
 
typedef long long LL;
const int N=100007;
 
struct Edge{
    int to,w;
    int next;
}p[200007];

int num;
int adj[N],dis[N],vis[N],cnt[N];
void addedge(int x,int y,int w)
{
    p[num].to=y;
    p[num].w=w;
    p[num].next=adj[x];
    adj[x]=num++;
}
 
bool spfa(int s,int n)
{
    fill(vis,vis+N,0);
    fill(cnt,cnt+N,0);
    queue<int> que;
    que.push(s);
    dis[s]=0;
    vis[s]=cnt[s]=1;
    while(!que.empty())
    {
        int u=que.front();
        que.pop();
        vis[u]=0;
        for(int i=adj[u];i!=-1;i=p[i].next)
        {
            int v=p[i].to;
            if(dis[v]>dis[u]+p[i].w)
            {
                dis[v]=dis[u]+p[i].w;
                if(!vis[v])
                {
                    vis[v]=1;
                    que.push(v);
                    cnt[v]++;
                    if(cnt[v]>n) return false;
                }
            }
        }
 
    }
    return true;
 
}
 
 
int main()
{
    int n,s,e;
    while(scanf("%d%d%d",&n,&s,&e)==3)
    {
        num=0;
        mem(adj,-1);
        int st,en,w;
        for(int i=1;i<=n;i++)
        {
            scanf("%d%d%d",&st,&en,&w);
            if(st<=e&&en>=s)
                addedge(max(st,s),min(en+1,e+1),w);
        }
 
        for(int i=e+1;i>=s;i--){
            addedge(i,i-1,0);
        }
        fill(dis+1,dis+1+e+1,INF);
        spfa(s,e+1-s+1);
        if(dis[e+1]!=INF) printf("%d\n",dis[e+1]);
        else
            printf("-1\n");
    }
    return 0;
}

'''



