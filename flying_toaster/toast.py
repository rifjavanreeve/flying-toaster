class Toast():
    
    roast_levels = {
        0: 'not toasted',
        1: 'slightly toasted',
        2: 'well toasted',
        3: 'heavily toasted',
        4: 'burned'
    }
    
    roast_level = 0

    def __init__(self, bread_type):
        self.bread_type = bread_type

    def is_toasted(self):
        return self.roast_level > 0
    
    def get_roast_level(self, seconds):
        if(seconds == 0):
            self.roast_level = 0
        elif(seconds <= 15):
            self.roast_level = 1
        elif(seconds <= 30):
            self.roast_level = 2
        elif(seconds <= 45):
            self.roast_level = 3
        elif(seconds > 45):
            self.roast_level = 4
    
    def rot(self):
        pass