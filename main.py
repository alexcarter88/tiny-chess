import json,os,urllib.request as u
U=os.environ["MAKEFUN_ENV_URL"]
V=(0,100,320,330,500,900,0)
C=(0,0,8,6,0,4,-15)
N=(33,31,18,14,-14,-18,-31,-33)
G=(1,-1,16,-16,15,17,-15,-17)
S=[0,0,N,G[4:],G[:4],G,G]
J=[(x,2)for x in N]+[(x,6)for x in G]
Q=lambda x:(int(x[1])-1)*16+ord(x[0])-97
A=lambda q:"abcdefgh"[q&7]+str((q>>4)+1)
K={0:13,4:12,7:14,112:7,116:3,119:11}
b=[0]*128;s=c=e=0;k=[0,0];T={}
def parse(f):
 global s,c,e
 b[:]=[0]*128;p=f.split();r=7;f=0
 for ch in p[0]:
  if ch=='/':r-=1;f=0
  elif ch.isdigit():f+=int(ch)
  else:v="pnbrqk".index(ch.lower())+1;b[r*16+f]=v+8*(ch>'Z');f+=1
 s=p[1]=='b';c=sum(1<<i for i,x in enumerate("KQkq")if x in p[2]);e=Q(p[3]) if p[3]!='-'else-1;k[0]=b.index(6);k[1]=b.index(14)
def att(q,y):
 o=8*y;d=4*o-16
 for t,w in[(d-1,1),(d+1,1)]+J:
  z=q+t
  if not z&136 and b[z]==w+o:return 1
 for t in G:
  z=q+t
  while not z&136 and not b[z]:z+=t
  if not z&136 and b[z]-o in(5,3+(abs(t)not in(15,17))):return 1
 return 0
def gen():
 m=[];d=16-32*s
 P=lambda t1:[q|t1<<7|p<<14 for p in(5,4,3,2)] if t1>>4==7-7*s else[q|t1<<7]
 for q in range(128):
  if q&136:continue
  v=b[q]
  if not v or v>>3!=s:continue
  t=v&7
  if t==1:
   t1=q+d
   if not t1&136 and not b[t1]:
    m+=P(t1)
    if q>>4==1+5*s and not b[t1:=q+2*d]:m.append(q|t1<<7)
   for t1 in(q+d-1,q+d+1):
    if t1&136:continue
    w=b[t1]
    if w and w>>3!=s:m+=P(t1)
    elif t1==e:m.append(q|t1<<7)
  else:
   for a in S[t]:
    t1=q+a
    while not t1&136:
     w=b[t1]
     if not w or w>>3!=s:m.append(q|t1<<7)
     if w or t%4==2:break
     t1+=a
 B=4+112*s
 for n in(1,-1):
  ro=3 if n>0 else-4
  if c&(1+(n<0))<<2*s and b[B+ro]==4+8*s and not b[B+n]and not b[B+2*n]and(n>0 or not b[B-3])and all(not att(B+i*n,s^1)for i in(0,1,2)):m.append(B|(B+2*n)<<7)
 return m
ST=[];NN=LM=AB=0
def make(m):
 global s,c,e
 f=m&127;t=m>>7&127;p=m>>14;v=b[f];w=b[t];cs=t;cap=w
 if v&7==1 and t==e and not w:cs=t-16+32*s;cap=b[cs];b[cs]=0
 ST.append((m,cap,cs,c,e,k[0],k[1]));b[f]=0;b[t]=p+8*s if p else v
 if v&7==6 and abs(t-f)==2:b[f+3 if t>f else f-4]=0;b[f+(t>f)-(t<f)]=4+8*s
 if v&7==6:k[s]=t
 c&=K.get(f,15)&K.get(t,15);e=(f+t)//2 if v&7==1 and abs(t-f)==32 else-1;s^=1
def unmake():
 global s,c,e
 m,cap,cs,c,e,k[0],k[1]=ST.pop();f=m&127;t=m>>7&127;p=m>>14;v=b[t];s^=1;b[t]=0;b[f]=1+8*s if p else v
 if v&7==6 and abs(t-f)==2:b[f+(t>f)-(t<f)]=0;b[f+3 if t>f else f-4]=4+8*s
 if cap:b[cs]=cap
def ev():
 z=0
 for q in range(128):
  if q&136 or not b[q]:continue
  v=b[q];t=v&7;r,f=q>>4,q&7;w=min(f,7-f)+min(r,7-r);a=V[t]+((r if v<8 else 7-r)*8 if t==1 else C[t]*w);z+=a if v<8 else-a
 return z*(1-2*s)
def order(ms,tm=0):
 return sorted(ms,key=lambda m:-((V[b[t]&7] if b[t:=m>>7&127] else 0)+(200000 if m>>14 else 0)+1000000*(m==tm)))
def sea(d,a,B):
 global NN,AB
 NN+=1
 if NN>=LM:AB=1;return 0
 tm=0;be=-100001
 if d<=0:
  if att(k[s],s^1):
   ms=gen()
   if not ms:return-100000
  else:
   be=ev()
   if be>=B:return be
   if be>a:a=be
   ms=[m for m in gen() if b[t:=m>>7&127] or m>>14 or b[m&127]&7==1 and t==e]
 else:
  key=(bytes(b),s,c,e,d);z=T.get(key)
  if z:
   v,fl,mv=z
   if fl==1 or fl==2 and v>=B or fl==3 and v<=a:return v
   tm=mv
  ms=gen();bm=0;a0=a
 for m in order(ms,tm):
  make(m)
  if att(k[s^1],s):unmake();continue
  z=-sea(max(d-1,0),-B,-a);unmake()
  if AB:return 0
  if z>be:be=z
  if d>0:bm=m
  if z>a:a=z
  if a>=B:break
 if be==-100001:return-100000 if att(k[s],s^1)else 0
 if d<=0:return be
 T[key]=(be,1+(be>=B)+(be<=a0)*2,bm)
 return be
def root(mv):
 global NN,LM,AB
 ms=[Q(x[:2])|Q(x[2:4])<<7|("nbrq".find(x[4:])+2)*(len(x)==5)<<14 for x in mv];be=ms[0]
 for d in range(12):
  NN=0;AB=0;LM=5e4;bs=-100001;bm=be
  for m in order(ms):
   make(m);z=-sea(d,-100001,100001);unmake()
   if AB:break
   if z>bs:bs=z;bm=m
  if AB:break
  be=bm
  if bs>99900:break
 return A(be&127)+A(be>>7&127)+"  nbrq"[be>>14].strip()
def post(p,d):return json.load(u.urlopen(U+p,json.dumps(d).encode()))
while True:
 g=post("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  parse(g["fen"]);g=post("/move",{"game":g["game"],"move":root(g["legal_moves"])})