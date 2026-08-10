# def myfunction(fname):
#     print(fname + "Aichum")

# myfunction("Saksit ") #ก็คือแทน ข้อความนี้เป็น fname
#---------------------------------------------------------


# def Sumnum(a,b):
#     func = (5 * a) + b
#     return func

# print(Sumnum(5,10))
#---------------------------------------------------------

# def get_box_area(w, l, h):
#     box = w * l * h
#     return box

# box1 = get_box_area(4,4,2)
# box2 = get_box_area(1,1,1)

# print(box1)
#---------------------------------------------------------


#---------------------------------------------------------
#สร้างฟังก์ชัน ข้อ 13
# def sayHello():
#     print("Hello Python")

# sayHello()

#สร้างฟังก์ชัน ข้อ 14
# def add(a,b):
#     plus = a + b
#     return plus

# print(add(10,20))

#สร้างฟังก์ชัน ข้อ 15 แบบเต็ม
# def checknum(num):
#     if num%2 == 0:
#         return "True"
#     else:
#         return "False"
    
# num = int(input("กรุณากรอกเลขขอคุณ : "))
# print(checknum(num))

# def is_even(num):
#     return num%2 == 0

# num = int(input("กรุณากรอกเลขของคุณ : "))
# print(is_even(num))
#---------------------------------------------------------

##DEF FUNCTION##
#4
# def multiply(a, b):
#     return a * b

# def square(num):
#     return num**2


# num = int(input("กรุณากรอกเลขของคุณ(ยกกำลัง) : "))
# a,b = map(int, input("กรุณากรอกเลขของคุณ(ผลคูณ ของเลข2ตัว) : ").split(","))

# print(f"ผลยกกำลังของคุณคือ {square(num)}")
# print(f"ผลคูณของคุณคือ {multiply(a,b)}")
#---------------------------------------------------------

#Mini Project
# def is_positive(num):
#     return num > 0

# def is_even(num):
#     return num%2==0

# def multiply(a,b):
#     return a * b

# while True:
#     print("\n------เมนู------")
#     print("1. เข้าเมนูเชคจำนวนบวกว่าเป็นจริงหรือไม่")
#     print("2. เข้าเมนูเชคเลขคู่")
#     print("3. เข้าเมนูหาผลคูณเลข 2 จำนวน")
#     print("4. ออกจากโปรแกรม")
    

#     choice = int(input("เลือกเมนู : "))

#     if choice == 1:
        
#         while True:
#             num = int(input("กรุณากรอกเลขของคุณ(กรอก 0 เพื่อหยุดการตรวจสอบ) : "))
        
#             if num == 0:
#                 print("หยุดการตรวจสอบ")
#                 break

#             print(is_positive(num))

#     elif choice == 2:
#         while True:
#             num = int(input("กรุณากรอกเลขของคุณ(กรอก 0 เพื่อหยุดการตรวจสอบ) : "))
        
#             if num == 0:
#                 print("หยุดการตรวจสอบ")
#                 break

#             print(is_even(num))

#     elif choice == 3:

#         while True:
#             num = input("กรอกเลข 2 ตัว (เช่น 5,10) หรือ 0 เพื่อออก : ")

#             if num == "0":
#                 print("ออกจากเมนูคูณ")
#                 break

#             a, b = map(int, num.split(","))
#             print(f"ผลลัพธ์ คือ {multiply(a, b)}")
            

#     elif choice == 4:
#         print("ออกจากโปรแกรม")
#         break

#     else:
#          print("กรุณาเลือกเมนู")
#---------------------------------------------------------

#ระดับ 3 : Function + Boolean
#สร้างฟังก์ชัน ถ้าคะแนนตั้งแต่ 50 ขึ้นไป คืนค่า True นอกนั้น False
# def ULscore(score):
#     return score >= 50

# while True:
#     score = int(input("กรุณากรอกคะแนนของคุณ : "))
#     if score == 0:
#         print("ออกจากโปรแกรม")
#         break

#     print(ULscore(score))
#---------------------------------------------------------

#ระดับ 4 : Function + if
# def grade(score):
#     if score >= 80:
#         return "Grade A"
#     elif score >= 70:
#         return "Grade B"
#     elif score >= 60:
#         return "Grade C"
#     elif score >= 50:
#         return "Grade D"
#     else:
#         return "Grade F"
    
# def max_number(a,b):
#     return max(a,b)

# while True:
#     score = int(input("กรุณากรอกคะแนนของคุณ(กรอก 0 เพื่อออกจากโปรแกรม) : "))
    
#     if score == 0:
#         print("ออกจากโปรแกรม")
#         break

#     print(grade(score))

# while True:
#     n0 = input("กรุณากรอกเลขของคุณ(กรอก 0 เพื่อออกจากโปรแกรม) : ")

#     if n0 == "0":
#         print("ออกจากโปรแกรม")
#         break

#     a,b = map(int, n0.split(","))
#     print(f"ผลลัพธ์ คือ {max_number(a,b)}")
#---------------------------------------------------------

#ระดับ 5 : Function + Loop
# def count_to_n(n):
#     for i in range(1, n+1):
#         print(i)

# def show_even(n1):
#     for i in range(2, n1+1, 2):
#         print(i)

# def sum_to_n(n2):
#     sum = 0
#     for i in range(1, n2+1):
#         sum += i
#     print(sum)

# n = int(input("กรุณากรอกเลขของคุณ(แสดงเลข1 ถึง n) : "))
# n1 = int(input("กรุณากรอกเลขของคุณ(แสดงเลขคู่) : "))
# n2 = int(input("กรุณากรอกเลขของคุณ(แสดงผลรวม) : "))


# count_to_n(n) #ใน loop มี print แล้วจึงไม่ต้องใส่print ในบรรทัดส่งออกอีก
# show_even(n1)
# sum_to_n(n2)
#---------------------------------------------------------


##ระดับ 6 : Mini Project
#ATM
# def show_balance(balance):
#     return balance

# def deposit(balance, depositt):
#     return balance + depositt

# def withdraw(balance, withdraww):
#     return balance - withdraww

# while True:
#     print("\n------เมนู------")
#     print("1. กรอกเงินในกระเป๋าเงินของคุณ")
#     print("2. ดูยอดเงิน")
#     print("3. ฝากเงิน")
#     print("4. ถอนเงิน")
#     print("5. ออกจากโปรแกรม")

#     choice = input("เลือกเมนูที่คุณต้องการ : ")
    

#     if choice == "1":
#         balance = float(input("กรุณากรอกเงินในบัญชี : "))
#         print("เงินของคุณคือ", balance, "บาท")
    
#     elif choice == "2":
#         print(show_balance(f"เงินของคุณคือ {balance} บาท"))

#     elif choice == "3":
#         depositt = float(input("กรุณากรอกจำนวนเงินที่จะฝาก : "))
#         balance = deposit(balance, depositt)
#         print(f"เงินของคุณปัจจุบัน คือ {balance} บาท")

#     elif choice == "4":
#         withdraww = float(input("กรุณากรอกจำนวนเงินที่จะถอน : "))

#         if withdraww > balance:
#             print("ยอดเงินไม่เพียงพอ")
#         else:
#             balance = withdraw(balance, withdraww)
#             print(f"เงินของคุณปัจจุบัน คือ {balance} บาท")

#     elif choice == "5":
#         print("ออกจากโปรแกรม")
#         break

#     else:
#         print("กรุณาเลือกเมนู ดังกล่าว")

# money = float(input("กรอกเงินในกระเป๋าของคุณ : "))
# depositt = float(input("กรอกจำนวนเงินที่คุณจะฝาก: "))
# withdraww = float(input("กรอกจำนวนเงินที่คุณจะถอน : "))
# 
# print(show_balance(money))
# print(deposit(money, depositt))
# print(withdraw(money, withdraww))
#---------------------------------------------------------

##ระดับ 6 : Mini Project
#สร้างโปรแกรมคำนวณพื้นที่
import math
def rectangle_area(width, height):
    return width * height

def triangle_area(base, height):
    return 1/2 * base * height

def circle_area(radius):
    return math.pi * (radius**2)

while True:
    print("\n------เมนู------")
    print("1. คำนวณพื้นที่สี่เหลี่ยม")
    print("2. คำนวณพื้นที่สามเหลี่ยม")
    print("3. คำนวณพื้นที่วงกลม")
    print("4. ออกจากโปรแกรม")

    choice = input("เลือกเมนูที่คุณต้องการ : ")

    if choice == "1":
        width, height = map(float, (input("กรุณากรอกความกว้างและความสูง : ").split(",")))
        # width, height = map(float, (
            # input("กรุณากรอกความกว้าง : "),
            # input("กรุณากรอกความสูง : ")
        # ))
        print(f"พื้นที่สี่เหลี่ยมนี้ คือ {rectangle_area(width, height)} ตารางเซนติเมตร")

    elif choice == "2":
        base, height = map(float, (input("กรุณากรอกฐานและความสูง : ").split(",")))
        print(f"พื้นที่สามเหลี่ยมนี้ คือ {triangle_area(base, height)} ตารางเซนติเมตร")

    elif choice == "3":
        radius = float(input("กรุณากรอกรัศมีของคุณ : "))
        print(f"พื้นที่วงกลมนี้ คือ {circle_area(radius):.2f} ตารางเซนติเมตร")

    elif choice == "4":
        print("ออกจากโปรแกรม")
        break

    else:
        print("กรุณากรอกเลขที่อยู่ในเมนู") 


# width = float(input("กรุณากรอกความกว้างของคุณ : "))
# height = float(input("กรุณากรอกความสูงของคุณ : "))
# base = float(input("กรุณากรอกฐานของคุณ : "))
# radius = float(input("กรุณากรอกรัศมีของคุณ : "))

# print(f"พื้นที่สีเหลี่ยมของคุณ คือ {rectangle_area(width, height)}")
# print(f"พื้นที่สามเหลี่ยมของคุณ คือ {triangle_area(base, height)}")
# print(f"พื้นที่วงกลมของคุณ คือ {circle_area(radius):.2f}")