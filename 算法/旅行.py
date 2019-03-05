#!/usr/bin/python
# -*- coding: utf-8 -*-

n, m, v = map(int, input().split())
list_d = []
for mm in range(m):
	x, y, z = map(int, input().split())
	list_d.append((x, y, z))

sort_d = sorted()
'''
#include <bits/stdc++.h>
#define maxn 19
int n,m,v,ans;
int chafen[maxn],a[maxn],b[maxn],t[maxn];
bool exsit[maxn];

using namespace std;
bool cheak(){//判断是否超载 
    int total=0;
    for(int i=1;i<=n;i++){
        total+=chafen[i];
        if(total>v)return 0; 
    }
    return 1;
}

void dfs(int dep){//每个站点都是上或不上人，总共2^m种方案
    if(dep==m+1){
        for(int i=1;i<=n;i++) chafen[i]=0;//初始化
        int temp=0;
        for(int i=1;i<=m;i++)
            if(exsit[i]){
                chafen[a[i]]+=t[i];//构造括号序列
                chafen[b[i]]-=t[i];
                temp+=(b[i]-a[i])*t[i];//计算当前方案总价钱 
             } 
         if(cheak())ans=max(ans,temp);//统计最大价钱
         return; 
    } 
    dfs(dep+1);
    exsit[dep]=1;//1代表上
    dfs(dep+1);
    exsit[dep]=0;//0代表不上
}

int main(){
    scanf("%d%d%d",&n,&m,&v);
    for(int i=1;i<=m;i++)
        scanf("%d%d%d",&a[i],&b[i],&t[i]);
    dfs(1);
    printf("%d\n",ans);
}

'''