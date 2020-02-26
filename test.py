import math
N,P,H,W=list(map(int,input().strip().split()));
pWord=list(map(int,input().strip().split()));
S=1;
while True:
    w,h=W//S,H//S;
    if w==0 or h==0:break;
    cols=0;
    for i in range(N):
        cols+=math.ceil(pWord[i]/w);
    if cols>h*P:break;
    S+=1;
print(S-1)
        
    