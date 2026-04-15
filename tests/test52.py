import random as r,time as t,sys,tty,termios
f=sys.stdin.fileno();d=[f'\033[{a}m{c}{v}\033[0m'for a,c in zip(range(91,95),'RGBY')for v in'0123456789']
p,a,o,s=r.sample(d,7),r.sample(d,7),r.choice(d),0
while p and a:
 T=termios.tcgetattr(f);tty.setraw(f);print(f"\033[H\033[JTop: {o}\nHand:",*(f'\033[7m{x}\033[0m'if i==s else x for i,x in enumerate(p)));k=sys.stdin.read(1)
 if k=='\x1b':k+=sys.stdin.read(2)
 termios.tcsetattr(f,2,T);s=(s+(k=='\x1b[C')-(k=='\x1b[D'))%len(p)
 if k in'\r\n ':
  c=p.pop(s)
  if{*c[5:7]}&{*o[5:7]}:
   o=c;s=0;t.sleep(.3);m=[x for x in a if{*x[5:7]}&{*o[5:7]}]
   if m:o=m[0];a.remove(o)
   else:a+=r.sample(d,1)
  else:p+=[c]+r.sample(d,1)
print("Win"if not p else"Lose")