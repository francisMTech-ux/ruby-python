class fruits:
    def __init__(self, price,shape,name):
        self.price = price
        self.shape = shape
        self.name = name
    def dispaly(self):
        print(f"my favourite fruit is {self.name} its {self.shape} in shape and cost {self.price}")

# create an instance of a class

myobj=fruits(price:20,shape:"oval",name:"banana")
myobj.dispaly()
