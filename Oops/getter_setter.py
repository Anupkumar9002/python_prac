class MyClass:
  def __init__(self, value):
        print("Hello")
        self._value = value
    
  def show(self):
    print(f"Value is {self._value}")
    
  @property             #getter function
  def ten_value(self):
      return 8* self._value
    
  @ten_value.setter
  def ten_value(self, new_value):
      self._value = new_value

obj = MyClass(9)
obj.ten_value = 67 # for setter method call
print(obj.ten_value)  #print getter output
obj.show()