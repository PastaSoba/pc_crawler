# クローリングしてくるパソコンのモデル

class PC_Model(object):
    def __init__(self, name=None, price=None, processor=None, memory=None, aquired_at=None):
        self.name = name
        self.price = price
        self.processor = processor
        self.memory = memory
        self.aquired_at = aquired_at

    @property
    def name(self):
        return self.name
    
    @property
    def price(self):
        return self.price
    
    @property
    def processor(self):
        return self.processor
    
    @property
    def memory(self):
        return self.memory
    
    @property
    def aquired_at(self):
        return self.aquired_at