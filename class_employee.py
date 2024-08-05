class Employee:
    __name=""
    __joindate=""
    __designation=""
    __salary=0
    
    def setData(self, name,joindate,designation,salary):
        self.__name = name
        self.__joindate = joindate
        self.__designation = designation
        self.__salary = salary
        
    def showData(self):
        print("name\t:",self.__name)
        print("daate of join\t:",self.__joindate)
        print("designation\t:",self.__designation)
        print("salary\t:",self.__salary)
 
def main():
         
         emp=Employee
         emp.setData('Mahek', '27-07-2024', 'clerk', 55000)
         emp.showdata()
         
if __name__=="__main__":
    main()
        
    