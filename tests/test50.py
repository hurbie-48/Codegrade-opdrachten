w=int(input());h=int(input());c=0
exec("print(*(c%10 for _ in range(w)));c+=w\n"*h)