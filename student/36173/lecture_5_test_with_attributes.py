#c)classs with attributes 
class Workers:
    company="Finance Solution"
    def __init__(self,first_name,last_name,nationality,period):
        self.first_name=first_name
        self.last_name=last_name
        self.nationality=nationality
        self.period=period
    def work_period(self):
        return f"{self.first_name} {self.last_name} has worked for {self.period}"
worker1=Workers("Rita","Gadlla","Swazi","2 years ")
worker2=Workers("elly","Salv","Polak","12 years")
print(worker1.work_period())
print(worker2.work_period())
