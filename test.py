num=list( map(int,input().strip().split(',')));
su=0;
maxn=0;
for i in num:
    su+=i;
    su = su if su>0 else 0;
    print('i:   ',maxn,su)
    maxn=max(maxn,su);
print(su)