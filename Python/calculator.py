
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result
    
    def mul(self, num):
        self.result *= num
        return self.result
    
    def div(self, num):
        self.result /= num
        return self.result
    
    def reset(self):
        self.result = 0
        return self.result
    
    def get_result(self):
        return self.result
    
    def set_result(self, num):
        self.result = num
        return self.result