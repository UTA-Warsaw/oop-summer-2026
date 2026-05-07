class TV:
    def __init__(self, volume_level):
        self.__volume_level = volume_level
    def increase_volume(self, x):
        if self.__volume_level <= 100:
            for i in range (x):
                print (self.__volume_level)
                self.__volume_level += 1
        else:
            print("Max volume is 100")
    def decrease_volume(self, y):
        if self.__volume_level > 0:
            for i in range (y):
                print (self.__volume_level)
                self.__volume_level = self.__volume_level - 1
        elif self.__volume_level == 0:
            print("Lowest volume is 0")
    def get_volume(self):
        print (f"The volume level right now is {self.__volume_level}")
       
sony_TV = TV(50)
#This is for example a buttons on remote control
sony_TV.increase_volume(20)
sony_TV.decrease_volume(10)
sony_TV.get_volume()

                
    
        