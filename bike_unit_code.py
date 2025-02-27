class Bike_sale:
    def __init__(self,bike_model= str, bike_cc=str):
        self.bike_model=bike_model
        self.bike_cc=bike_cc
        self.insurance=[]
        #self.accessories=[]
        self.price=1000 if self.bike_model=="Classic" else 500 if self.bike_model=="Bullet" else 250
        self.price+=1000 if self.bike_cc=="750" else 500 if self.bike_cc=="500" else 350
    def bike_insurance(self, insure: str):
        self.insurance.append(insure) 
        self.price+=200 
    def bike_accessories(self):
        access=["Seat","Foot rest", "Mirror"]
        access.append("Rider Jacket") if self.bike_cc=="750" else access.append("Riding helmet") if self.bike_cc=="500" else access.append("Riding Glass")
        access+=self.insurance
        return access
    def check_price(self)->float:
        return self.price
    
Bike=Bike_sale("Classic", "500")
Bike.bike_insurance("Added")
#Bike.bike_accessories("750")
bike_list=Bike.bike_accessories()
bike_price=Bike.check_price()

print(bike_list,bike_price)


