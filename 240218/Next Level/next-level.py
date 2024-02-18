class Info:
    def __init__(self,dd,lv):
        self.dd=dd
        self.lv=lv
    

co = Info("codetree","10")
d,l =input().split()
new= Info(d,l)

print(f"user {co.dd} lv {co.lv}")
print(f"user {new.dd} lv {new.lv}")