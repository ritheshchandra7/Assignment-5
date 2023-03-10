
# Implement the Complete Student Class

class Student:
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def setRollNumber(self,RollNumber):
        self.__RollNumber=RollNumber
    def getRollNumber(self):
        return self.__RollNumber

obj=Student()
obj.setName("Rithesh Chandra")
obj.setRollNumber(293)
print("The name of the student is: ",obj.getName())
print("The roll number of the student is: ",obj.getRollNumber())