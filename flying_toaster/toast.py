class Toast():
    #TODO Toast class
    roast_levels = {
        0: 'not toasted',
        1: 'slightly toasted',
        2: 'well toasted',
        3: 'heavily toasted',
        4: 'burned'
    } # TODO: roast levels
    
    roast_level = 0

    def __init__(self, bread_type):
        self.bread_type = bread_type

    def is_toasted(self):
        return self.roast_level > 0
    
    def rot(self):
        pass