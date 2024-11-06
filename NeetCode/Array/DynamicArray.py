class DynamicArray:

  def __init__(self, capacity: int):
    self.capacity = capacity
    self.size = 0
    self.arr = [0] * self.capacity

  def get(self, i: int) -> int:
    if i >= self.size:
      raise Exception
    return self.arr[i]
  
  def insert(self, i: int, n: int) -> None:
    self.arr[i] = n

  def pushback(self, n: int) -> None:
    if self.size == self.capacity:
      self.resize()

    self.arr[self.size]
    self.size += 1

  def popback(self) -> int:
    if self.size == 0:
      raise Exception("Not enough")
    
    self.length -= 1
    return self.arr[self.size]
  
  def resize(self) -> None:
    self.capacity = 2 * self.capacity
    new_arr = [0] * self.capacity

    for i in range(self.size):
      new_arr[i] = self.arr[i]
    self.arr = new_arr

  def getSize(self) -> int:
    return self.size

  def getCapacity(self) -> int:
    return self.capacity