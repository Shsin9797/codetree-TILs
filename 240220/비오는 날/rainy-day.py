class Weather:
    def __init__(self,date,day,weather):
        self.date=date
        self.day=day
        self.weather=weather

n= int(input())
nlist=[]
for _ in range(n):
    date,day,weather = input().split()
    w = Weather(date,day,weather)
    if w.weather =="Rain":
        nlist.append(w)


short = nlist[0].date 
idx=0
for i in range(len(nlist)):
    w= nlist[i]
    if w.date < short: 
        short = w.date
        idx =i 

p = nlist[idx]
print(p.date,p.day,p.weather)