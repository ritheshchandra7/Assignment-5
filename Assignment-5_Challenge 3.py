#Implement the Complete Student Class
class Student:
  __name = None
  __rollNumber =None

  def setName(self,name):
   self.__name = name
  def getName(self):
    return self.__name

  def setRollNumber(self, rollNumber):
    self.__rollNumber = rollNumber

  def getRollNumber(self):
    return self.__rollNumber


result = Student()
result.setName("More Rithesh Chandra")
print("Name:", result.getName())
result.setRollNumber(293)
print("Roll Number:", result.getRollNumber())