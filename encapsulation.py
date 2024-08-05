class calculator:
    def set_value(self,new_value):
        """set a new value for the calculator."""
        self._value = new_value
if __name__ == " __main__":
    calc = calculator()
    
    calc.add(10)
    print("After adding 10:",calc.get_value())
    
    calc.subtract(5)
    print("After subtracting 5:",calc.get_value())
    
    calc.set_value(100)
    print("After setting value to 100:",calc.get_value())
    
    