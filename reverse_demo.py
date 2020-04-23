import os
class ReverseDemo:
  def __init__(self):
    self.reverse_string = ""

  def reverse(self,string):
    for i in range(-1,-(len(string)+1),-1):
      self.reverse_string += string[i]
    return self.reverse_string


user_input = input("Please input a string")
t = ReverseDemo()
print(t.reverse(user_input))
os.system("pause")