class Product:
    def __init__(self,name="codetree",code="50"):
        self.name=name
        self.code=code


n,c= input().split()
pro1= Product()
pro2= Product(n,c)

for a in [pro1,pro2]:
    print(f"product {a.code} is {a.name}")