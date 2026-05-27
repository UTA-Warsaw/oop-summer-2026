class CardDetails:
    def __init__(self,name,card_type,card_number):
        self.name = name
        self.card_type= card_type
        self.card_number= card_number
p1 = CardDetails("kara","debit card", 45572384677)
print(p1.name)
print(p1.card_number)
print(p1.card_type)
