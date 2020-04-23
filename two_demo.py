import os
class TwoDemo:
  def __init__(self):
    self.number = 0

  def compute(self,num):
    for i in range(0,num,):
      if i%3==0 and i%5==0:
        self.number += 1
      elif i%3==0 or i%5==0:
        continue
      else:
         self.number += 1
    return self.number

try:
    user_input = int(input("Please input an integer"))
    t = TwoDemo()
    print(t.compute(user_input))
except ValueError:
    print("you input not an integer")

os.system("pause")