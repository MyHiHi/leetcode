#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
struct node{
    int a,b;
    node(){}
    node(int x,int y):a(x),b(y){}
};
bool cmp(node x,node y){
    if (x.a==y.a)
    return x.b<y.b;
    else
        return x.a<y.a;
}
int main(){
    int n;
    cin>>n;
    vector<node>area(n);
    for(int t=0;t<n;t++){
        int a,b;
        cin>>a>>b;
        area[t]=node(a,b);
    }
    sort(area.begin(),area.end(),cmp);
    int cnt=2;
    int l=area[0].a,r=area[0].b;
    for (int t=1;t<n;t++){
        node c=area[t];
        if(c.a>=l && c.a<=r){
            l=c.a;
            r=min(r,c.b);
        }else{
            cnt+=2;
            l=c.a;
            r=c.b;
        }
    }
    cout<<cnt;
    return 0;
}

