# ##CLASS
# class Employee():

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def showdata(self):
#         print(f"ชื่อพนักงาน : {self.name}")
#         print(f"เงินเดือนที่ได้ : {self.salary}")



# ##OPJECT
# emp1 = Employee("Pahan", 35000) 
# # print(f"ชื่อพนักงาน : {emp1.name}")
# # print(f"เงินเดือนที่ได้ : {emp1.salary}")
# emp1.salary += 5000
# emp1.showdata()
# ---------------------------------------------------------------------------

#โจทย์self.balance -= amount
# class BackAccount():
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"ฝากเงิน {amount} บาท สำเร็จ ยอดเงินคงเหลือ {self.balance} บาท")


#     def withdraw(self, amount):
#         if self.balance < amount:
#             print("ยอดเงินไม่เพียงพอ")
#         else:
#             self.balance -= amount
#             print(f"ฝากเงิน {amount} บาท สำเร็จ ยอดเงินคงเหลือ {self.balance} บาท")

#     def show_balance(self):
#         print(f"มียอดเงินทั้งหมด {self.balance}")


# account = BackAccount("Saksit", 1000)


# account.deposit(500)
# account.withdraw(300)
# account.show_balance()
#---------------------------------------------------------------------------

##Function เสริม##
# class Employee():

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def showdata(self):
#         print(f"ชื่อพนักงาน : {emp1.name}")
#         print(f"เงินเดือนที่ได้ : {emp1.salary}")

# ##OPJECT
# emp1 = Employee("Pahan", 35000) 
# # print(f"ชื่อพนักงาน : {emp1.name}")
# # print(f"เงินเดือนที่ได้ : {emp1.salary}")
# emp1.salary += 5000
# emp1.showdata()

## print(isinstance(emp1, Employee)) #เชคว่าตัว emp1 นี้เป็นสมาชิกของคลาส Employee หรือไม่
## print(dir(emp1)) #เชคว่าตัว emp1 มี method อะไรบ้าง
## print(emp1.__class__) #เชคว่าตัว emp1 เป็นคลาสอะไร
#---------------------------------------------------------------------------

##การห่อหุ้มข้อมูล (Encapsulation) คือการซ่อนรายละเอียดของข้อมูลและฟังก์ชันภายในคลาส เพื่อป้องกันการเข้าถึงโดยตรงจากภายนอกคลาส ข้อดี = เนื่องจากจะถูกเข้าถึงเฉพาะคนที่มีสิทธิ์เท่านั้น
# protected ---._--- คือ สามารถแก้ไขได้
# private ---.__--- คือ ไม่สามารถแก้ไขได้
#---------------------------------------------------------------------------

##Getter,Setter Method
# Setter คือ การกำหนดค่าให้ Object
# Getter คือ การดึงค่าจาก Object
#---------------------------------------------------------------------------

##=== Getter,Setter ===
# class Employee:
#     def __init__(self, name, salary, department):
#         self.__name = name
#         self.__salary = salary
#         self.department = department
        
#     def showInfo(self):
#         print(f"ชื่อพนักงาน : {self.__name}")
#         print(f"เงินเดือน : {self.__salary}")
#         print(f"แผนก : {self.department}")

#     ##Setter
#     def setName(self, newname):
#         self.__name = newname

#     def setSalary(self, newsalary):
#         self.__salary = newsalary

#     ##Getter จะได้ไม่ต้องไปดึง Object โดยตรง แล้ว
#     def getName(self):
#         return self.__name

# emp1 = Employee("Maja", 12345, "Sale")
# #emp1.setName("Siuu")
# emp1.setSalary(15000)
# emp1.showInfo()
# print(emp1.getName())
#---------------------------------------------------------------------------

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance

#     def showInfo(self):
#         print(f"ชื่อคุณ {self.owner} มีเงิน {self.__balance} บาท")

#     def setBalance(self, newBalance):
#         if newBalance < 0:
#             print("ยอดเงินห้ามติดลบ")
#         else:
#             self.__balance = newBalance
        
#     def get_Balance(self):
#         return self.__balance
    
#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"ชื่อ {self.owner} ได้ทำการฝากเงินเข้า {amount} บาท")

#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print("ยอดเงินไม่เพียงพอ")    
#         else:
#             self.__balance -= amount
#             print(f"ชื่อ {self.owner} ได้ทำการถอนเงินออก {amount} บาท")
        


# Owner = BankAccount("John", 1000)

# Owner.deposit(10000)
# Owner.withdraw(11111)

# Owner.showInfo()
#---------------------------------------------------------------------------

##Mini project OOP
# class Student:
#     def __init__(self, name, score, age):
#         self.name = name
#         self.score = score
#         self.age = age

#     def show_info(self):
#         print("\n====ข้อมูลนักเรียน====")
#         print(f"ชื่อนักเรียน คือ {self.name}")
#         print(f"คะแนนของคุณ คือ {self.score}")
#         print(f"อายุของคุณคือ {self.age}")

#     def update_score(self, new_score):
#         self.score = new_score
#         print(f"คะแนนของ {self.name} ถูกเปลี่ยนเป็น {self.score} เรียบร้อยแล้ว")

#     def is_pass(self):
#         if self.score >= 50:
#             print("คุณสอบผ่าน")
#         else:
#             print("คุณสอบไม่ผ่าน")



# stu = Student("Pahan", 100, 20)
# stu.show_info()
# new_score = int(input("กรอกคะแนนใหม่ของคุณ : "))
# stu.update_score(new_score)
# stu.is_pass()
#---------------------------------------------------------------------------

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def __str__(self):
#         return f"Rectangle ({self.width} x {self.height})"

#     def area(self):
#         return self.width * self.height
    
#     def perimeter(self):
#         return 2 * (self.width + self.height)

#     def is_square(self):
#         return self.width == self.height

# width, height = map(int, input("กรอกความกว้าง, ความสูง : ").split(","))
# rect = Rectangle(width, height)

# print(rect)
# print(f"พื้นที่ = {rect.area()} ตารางเซนติเมตร")
# print(f"พื้นที่รอบรูป = {rect.perimeter()} เซนติเมตร")
# print(f"มีค่าความจริงเป็น {rect.is_square()}")
#---------------------------------------------------------------------------

##Student Management System(OOP Version)
# class Student:
#     def __init__(self, name, score, age):
#         self.name = name
#         self.score = score
#         self.age = age
    
#     def show_info(self):
#         print(f"\nชื่อนักเรียน : {self.name}") 
#         print(f"คะแนนที่ได้ : {self.score} คะแนน") 
#         print(f"อายุ : {self.age} ปี")
#         print()
        
#     def update_score(self, new_score):
#         self.score = new_score
#         print(f"นักเรียนที่ชื่อ {self.name} ได้แก้ไขคะแนนเป็น {self.score}")

#     def is_pass(self):
#         if self.score >= 50:
#             print("สอบผ่าน")
#         else:
#             print("สอบไม่ผ่าน")


# lstStudent = []
# while True:
#     print("\n====Menu====")
#     print("1. เพิ่มนักเรียน")
#     print("2. ดูนักเรียนทั้งหมด")
#     print("3. แก้ไขคะแนน")
#     print("4. ตรวจสอบว่าสอบผ่านมั้ย")
#     print("5. ออกจากโปรแกรม")

#     choice = input("กรอกเมนูที่ต้องการ : ")

#     if choice == "1": #Function Add Data
#         name = input("กรอกชื่อนักเรียน : ") #Variable name
#         score = float(input("กรอกคะแนนนักเรียน : ")) #Variable score
#         age = int(input("กรอกอายุนักเรียน : ")) #Variable age

#         student = Student(name, score, age) #Variable add student(name, score, age)

#         lstStudent.append(student) #Append to list
        
#         print("เพิ่มข้อมูลเรียบร้อย")

#     elif choice == "2": #Function Show Data
#         for student in lstStudent:
#             student.show_info()

#     elif choice == "3":
#         name = input("กรอกชื่อนักเรียนที่จะแก้ไข : ")
#         for student in lstStudent:
#             if student.name == name:
#                 new_score = int(input("กรอกคะแนนใหม่ : "))
#                 student.update_score(new_score)
#             else:
#                 print("ไม่พบข้อมูล")

#     elif choice == "4":
#         for i, student in enumerate(lstStudent, start=1):
#             print(f"\nคนที่ {i}")
#             student.is_pass()

#     elif choice == "5":
#         print("ออกจากโปรแกรม")
#         break

#     else:
#         print("กรุณาเลือกให้ตรงกับเมนู")
#---------------------------------------------------------------------------

##Library Management System(OOP Version) Miniproject 2
# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def show_info(self):
#         print(f"ชื่อหนังสือ : {self.title}")
#         print(f"ชื่อผู้แต่ง : {self.author}")
#         print(f"ราคา : {self.price}")

#     def update_price(self, new_price):
#         self.price = new_price
#         print(f"แก้ไขราคาจากหนังสือเรื่อง {self.title} เป็นราคา {self.price} บาท")

#     def discount(self, percent):
#         self.price -= self.price * (percent / 100)
#         print(f"ลดราคาไป {percent} เปอร์เซ็นต์ ดังนั้นจะเหลือที่ต้องจ่าย {self.price} บาท")

#     def is_expensive(self):
#         if self.price >= 1000:
#             print("หนังสือเล่มนี้ ราคาแพง")
#         else:
#             print("หนังสือเล่มนี้ ราคาปกติ")

# books = []
# while True:
#     print(f"\n=====Library=====")
#     print(f"1. เพิ่มหนังสือ")
#     print(f"2. ดูหนังสือทั้งหมด")
#     print(f"3. เปลี่ยนราคา")
#     print(f"4. ลดราคา")
#     print(f"5. ค้นหาหนังสือ")
#     print(f"6. ลบหนังสือ")
#     print(f"7. ออกจากโปรแกรม")

#     choice = input("เลือกเมนูที่ต้องการ : ")

#     if choice == "1":
#         title = input("กรอกชื่อหนังสือ : ")
#         auther = input("กรอกชื่อผู้แต่ง : ")
#         price = int(input("กรอกราคา : "))

#         book = Book(title, auther, price)
#         books.append(book)

#         print("เพิ่มข้อมูลเรียบร้อย")

#     elif choice == "2":
#         for i,book in enumerate(books, start=1):
#             print(f"\nหนังสือเล่มที่ {i}")
#             book.show_info()
#             book.is_expensive()

#     elif choice == "3":
#         title = input("กรอกชื่อหนังสือที่จะเข้าไปแก้ไขราคา : ")
#         for bk in books:
#             if bk.title == title:
#                 new_price = float(input("กรอกคะแนนใหม่ : "))
#                 bk.update_price(new_price)

#     elif choice == "4":
#         title = input("กรอกชื่อหนังสือที่จะลดราคา : ")
#         for bk in books:
#             if bk.title == title:
#                 discountPer = float(input("กรอกเปอร์เซ็นที่จะลด : "))
#                 bk.discount(discountPer)

#     elif choice == "5":
#         title = input("กรอกชื่อหนังสือที่จะค้นหา : ")
#         for bk in books:
#             if bk.title == title:
#                 bk.show_info()
#             else:
#                 print("ไม่พบข้อมูล")
        
#     elif choice == "6":
#         title = input("กรอกชื่อหนังสือที่จะค้นหา : ")
#         for bk in books:
#             if bk.title == title:
#                 books.remove(bk)
#                 print("ทำการลบข้อมูลเรียบร้อย")

#     elif choice == "7":
#         print("ออกจากโปรแกรม")
#         break

#     else:
#         print("กรุณาเลือกให้ตรงกับเมนู")

# # bk1 = Book("นิทาน", "ซาร่า", 1400)
# # bk1.show_info()
# # np = int(input("กรอกราคาใหม่ : "))
# # bk1.update_price(np)
# # bk1.show_info()

# # ds = int(input("กรอกราคาที่จะลด : "))
# # bk1.discount(ds)
# # bk1.show_info()
#---------------------------------------------------------------------------------------------------------------------------

##การสืบทอดคุณสมบัติ (Inheritance)
# คลาสแม่(Superclass) คลาสลูก(Subclass) คุณสมบัติต่างๆจากคลาสแม่จะถูกถ่ายทอดไปยังลูก
#คลาสแม่ class Employee: , คลาสลูก class Programmer(Employee)
#Keyword super คือ เมื่อต้องการใช้คุณสมบัติต่างๆของ class แม่ เช่น Constructure, Method, Atrribute
#super().__init__(===)

##การแปลง Object ให้เป็น String
#def __str__(self):
#    return "ชุดข้อความ"

#---------------------------------------------------------------------------

# class Vehicle():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def showInfo(self):
#         print(f"{self.make} {self.model} {self.year}")

# class Car(Vehicle):
    
#     def __init__(self, make, model, year, quanityDoor):
#         super().__init__(make, model, year)
#         self.quanityDoor = quanityDoor

#     def showInfo(self):
#         super().showInfo()
#         print(f"{self.quanityDoor} doors")

# car1 = Car("Ford", "Mustang", 2026, 2)
# car1.showInfo()
#---------------------------------------------------------------------------

# class Employee:
#     def __init__(self, name, salary, department):
#         self.name = name
#         self.salary = salary
#         self.department = department
        
#     def showInfo(self):
#         print(f"ชื่อพนักงาน : {self.name}")
#         print(f"เงินเดือน : {self.salary}")
#         print(f"แผนก : {self.department}")

#     def salaperyear(self):
#         return self.salary * 12

#     #Object เป็น String
#     def __str__(self):
#         return (f"ชื่อพนักงาน = {self.name}, มีเงินเดือน = {self.salary} บาท, แผนก = {self.department} และมีรายได้รายปีเท่ากับ {self.salaperyear()} บาท")


# class Accounting(Employee):

#     department = "แผนกบัญชี"

#     def __init__(self, name, salary):
#         super().__init__(name, salary, self.department)

#     def showInfo(self):
#         return super().showInfo()

# class Programmer(Employee):

#     department = "แผนกไอที"

#     def __init__(self, name, salary):
#         super().__init__(name, salary, self.department)

#     def showInfo(self):
#         return super().showInfo()

# class Sale(Employee):

#     department = "แผนกขาย"

#     def __init__(self, name, salary):
#         super().__init__(name, salary, self.department)

#     def showInfo(self):
#         return super().showInfo()


# account = Accounting("ป่าน", 15000)
# #account.showInfo()
# #print(f"รายได้ต่อปี ได้ {account.salaperyear()} บาท")
# print(account.__str__())


# programmer = Programmer("ฟิล์ม", 50350)
# #programmer.showInfo()
# #print(f"รายได้ต่อปี ได้ {programmer.salaperyear()} บาท")
# print(programmer.__str__())


# saleMan = Sale("นาย", 9000)
# #saleMan.showInfo()
# #print(f"รายได้ต่อปี ได้ {saleMan.salaperyear()} บาท")
# print(saleMan.__str__())

#---------------------------------------------------------------------------

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def showDATA(self):
#         print(f"ชื่อ {self.name} และมีอายุ {self.age} นั้น")

#     def eat(self):
#         print("กำลังกินอาหาร")

#     def sleep(self):
#         print("กำลังนอน")

#     def sound(self):
#         return "สัตว์ส่งเสียง"
#         #print("สัตว์ส่งเสียง")

# class Dog(Animal):
#     #def bark(self):
#     #    print("กำลังเห่า")
#     def sound(self):
#         return f"{super().sound()} โฮ่ง โฮ่ง"
#         #print("โฮ่ง โฮ่ง")
    
# class Cat(Animal):
#     #def meow(self):
#     #    print("เหมียว เหมียว")
#     def sound(self):
#         return f"{super().sound()} เหมียว เหมียว"
#         #print("เหมียว เหมียว")

# class Bird(Animal):
#     def fly(self):
#         return("กำลังบินนน")
    
#     def sound(self):
#         return f"{super().sound()} จิ๊บ จิ๊บ"
#         #print("จิ๊บ จิ๊บ")


# print("="*30)

# dog = Dog("Jason", 2)
# dog.showDATA()
# dog.eat()
# dog.sleep()
# print(dog.sound())

# print("="*30)

# cat = Cat("Mui",4)
# cat.showDATA()
# print(cat.sound())

# print("="*30)

# bird = Bird("Maja", 3)
# bird.showDATA()
# bird.eat()
# bird.fly()
# print(bird.sound())
#---------------------------------------------------------------------------

##พหุสัณฐาน Polymorphism
#Overloading method คือ Method ที่มีชื่อเหมือนกันและอยู่ภายในคลาสเดียวกัน สรุป นิยาม Method ชื่อเดียวกัน รับพารามิเตอร์ต่างกันได้ 
#Overriding method คือ class ลูก มีชื่อเหมือนกัน class แม่
##ก็แค่เพิ่มต่อจาก Class การสืบทอด แล้วต้อง show ทุกอัน
# class Employee:
#     def __init__(self, name, salary, department):
#         self.name = name
#         self.salary = salary
#         self.department = department
        
#     def showInfo(self):
#         print(f"ชื่อพนักงาน : {self.name}")
#         print(f"เงินเดือน : {self.salary}")
#         print(f"แผนก : {self.department}")

#     def salaperyear(self):
#         return self.salary * 12

#     #Object เป็น String
#     def __str__(self):
#         return (f"ชื่อพนักงาน = {self.name}, มีเงินเดือน = {self.salary} บาท, แผนก = {self.department} และมีรายได้รายปีเท่ากับ {self.salaperyear()} บาท")


# class Accounting(Employee):

#     department = "แผนกบัญชี"
#     #เพิ่มอายุ overloading
#     def __init__(self, name, salary, age):
#         super().__init__(name, salary, self.department)
#         self.age = age

#     #overiding
#     def showInfo(self):
#         super().showInfo()
#         print(f"อายุ : {self.age} ปี")

#     def __str__(self):
#         return (super().__str__())

# class Programmer(Employee):

#     department = "แผนกไอที"
#     #เพิ่มประสบการทำงานและสกิล overloading 
#     def __init__(self, name, salary, experience, skill):
#         super().__init__(name, salary, self.department)
#         self.experience = experience
#         self.skill = skill

#     #overiding
#     def showInfo(self):
#         super().showInfo()
#         print(f"ประสบการณ์ทำงาน : {self.experience} ปี")
#         print(f"สกิล : {self.skill}")

# class Sale(Employee):

#     department = "แผนกขาย"
#     #เพิ่มเขตพื้นที่ overloading
#     def __init__(self, name, salary, area):
#         super().__init__(name, salary, self.department)
#         self.area = area

#     #overiding
#     def showInfo(self):
#         super().showInfo()
#         print(f"พื้นที่รับผิดชอบ : {self.area}")


# account = Accounting("ป่าน", 15000, 21)
# #account.showInfo()
# #print(f"รายได้ต่อปี ได้ {account.salaperyear()} บาท")
# account.showInfo()
# print("="*30)


# programmer = Programmer("ฟิล์ม", 50350, 0.6, "Python code")
# #programmer.showInfo()
# #print(f"รายได้ต่อปี ได้ {programmer.salaperyear()} บาท")
# programmer.showInfo()
# print("="*30)

# saleMan = Sale("นาย", 9000, "Agentina")
# #saleMan.showInfo()
# #print(f"รายได้ต่อปี ได้ {saleMan.salaperyear()} บาท")
# saleMan.showInfo()
# print("="*30)
#---------------------------------------------------------------------------

#### Final ####
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def displayData(self):
        print(f"ชื่อ {self.name} ได้เงินเดือน {self.salary} บาท")

    def work(self):
        print("พนังงานกำลังทำงาน")

class Programmer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        
    def work(self):
        super().work()
        print("กำลังเขียนโปรแกรม")

class Designer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def work(self):
        super().work()
        print("กำลังออกแบบ UI")

programmer = Programmer("John", 52000)
programmer.displayData()
programmer.work()
print("="*30)

designer = Designer("AD", 20000)
designer.displayData()
designer.work()
print("="*30)