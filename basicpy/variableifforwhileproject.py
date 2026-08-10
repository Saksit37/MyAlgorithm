##Variable + input + output
#รับชื่อผู้ใช้จากคีย์บอร์ด แล้วแสดงข้อความ
# name = input("กรอกชื่อของคุณ : ")
# print(f"สวัสดี {name}")


#รับตัวเลข 2 จำนวน แล้วแสดงผลบวก
# num0 = int(input("กรอกตัวเลขที่ 1 : "))
# num1 = int(input("กรอกตัวเลขที่ 2 : "))
# print(f"ผลบวก คือ {num0+num1}")


#รับชื่อสินค้า ราคา และจำนวนสินค้า ------ คำนวณราคารวม
# product = input("ชื่อสินค้า : ")
# price = float(input("ราคา (บาท) : "))
# quantity = int(input("จำนวน (ชิ้น) : "))
# total = price * quantity
# print(f"ราคารวม : {total} บาท")

#----------------------------------------------------------

##If/ elif/ else
#รับคะแนนสอบ
# score = int(input("กรอกคะแนนของคุณ : "))
# if score >= 80:
    # print("Grade A")
# elif score >= 70:
    # print("Grade B")
# elif score >= 60:
    # print("Grade C")
# else:
    # print("Grade F")


#รับอายุ
# age = int(input("กรอกอายุของคุณ : "))
# if age < 13:
#     print("เด็ก")
# elif age >= 13 and age <= 19:
#     print("วัยรุ่น")
# elif age >= 20:
#     print("ผู้ใหญ่")


#รับตัวเลข 1 จำนวน
# rannum = int(input("กรอกตัวเลขของคุณ : "))
# if rannum < 0:
#     print("จำนวนเต็มลบ")
# elif rannum > 0:
#     print("จำนวนเต็มบวก")
# else:
#     print("จำนวนเต็มศูนย์")

#----------------------------------------------------------

##For loop
#แสดงตัวเลข 1 ถึง 10
# rdnum = int(input("กรอกเลขที่คุณต้องการ : "))
# for i in range(1,rdnum+1):
#     print(i)


#รับตัวเลข n แสดงผลรวมตั้งแต่ 1 ถึง n
# n = int(input("กรอกเลขที่คุณต้องการ : "))
# sum = 0
# for i in range(1, n+1):
#     sum += i
#     print(sum)


#สร้างสูตรคูณแม่ n
# multiplicationTable = int(input("กรอกสูตรคูณแม่ที่คุณต้องการ : "))
# for i in range(1, 13):
#     print(f"{multiplicationTable} x {i} = {multiplicationTable*i}")

#----------------------------------------------------------

##While Loop
#นับเลข 1 ถึง 10 ด้วย while
# i = 1 #เริ่มที่ 1
# while i <= 10:#ถึง10
#     print(i)
#     i += 1
#แสดงเลขคู่ตั้งแต่ 2 ถึง 20
# i = 2
# while i <= 20:
#     print(i)
#     i += 2
# n = int(input("กรอกเลขที่ต้องการ : "))
# i = 1
# while i <= n:
#     print(i, end=" ")
#     i += 1

#ให้ผู้ใช้กรอกรหัสผ่าน ถ้ากรอกผิดให้ถามใหม่เรื่อยๆ รหัสผ่านที่ถูกต้องคือ admin123
# while True:
#     pswd = input("กรอกรหัสผ่านของคุณ : ")

#     if pswd == "admin123":
#         print("PASSWORD CORRECT")
#         break
#     else:
#         print("PASSWORD WRONG")

#ให้ผู้ใช้กรอกตัวเลขไปเรื่อย ๆ ถ้ากรอก 0 ให้หยุดโปรแกรม และแสดงผลรวมของตัวเลขทั้งหมด
# sum = 0
# while True:
#     num = int(input("กรอกเลขของคุณ : "))
#     if num == 0:
#         break

#     sum += num
# print(f"ผลรวม = {sum}")

#-------------------------------------------------------------------------
###ทบทวนก่อนเข้าเรื่อง Function, List###
#โจทย์ที่ 1 : เครื่องคิดเลขอย่างง่าย
# n = int(input("กรอกเลขที่คุณต้องการตัวที่ 1 : "))
# n1 = int(input("กรอกเลขที่คุณต้องการตัวที่ 2 : "))
# n2 = input("เลือกเครื่องหมาย : ")

# if n2 == "+":
#     total = n + n1
# elif n2 == "-":
#     total = n - n1
# elif n2 == "*":
#     total = n * n1
# elif n2 == "/":
#     total = n / n1

# print(f"ผลลัพธ์ = {total}")


#โจทย์ที่ 2 : ตรวจสอบเลขคู่เลขคี่
# num = int(input("กรอกเลขของคุณ : "))
# if num%2 == 0:
#     print("This is Even")
# else:
#     print("This is Odd")


#โจทย์ที่ 3 : ตารางสูตรคูณ
# multiplicationTable = int(input("กรอกเลขที่อยากจะให้หาแม่สูตรคูณ : "))
# for i in range(1, 13):
#     print(f"{multiplicationTable} x {i} = {multiplicationTable*i}")


#โจทย์ที่ 4 : หาผลรวมเลขคู่ #for ค่าที่ต้องบวกไปเรื่อยๆเช่น sum+=i ต้องอยู่ก่อน
# num = int(input("กรอกเลขที่คุณต้องการ : "))
# sum = 0
# for i in range(2, num+1, 2):
#     sum += i
# print(f"ผลรวม = {sum}")


#โจทย์ที่ 5 : เดารหัสผ่าน
# while True:
#     txt = input("กรอกรหัสผ่านของคุณ : ")

#     if txt == "python123":
#         print("PASSWORD CORRECT")
#         break
#     else:
#         print("PASSWORD WRONG")


#โจทย์ที่ 6 : เครื่องบวกเลขสะสม
# sum = 0
# count = 0
# while True:
#     rdnum = int(input("กรอกเลขของคุณ : "))

#     if rdnum == 0:
#         break

#     sum += rdnum
#     count += 1
# print(f"ผลลัพธ์คือ {sum}")
# print(f"จำนวน {count} ครั้ง")


#โจทย์ที่ 7 : เกมทายเลข
# while True:
#     randomnum = int(input("กรอกเลขของคุณ : "))
#     secret = 7
#     if randomnum < secret:
#         print("น้อยเกินไป") 
#     elif randomnum > secret:
#         print("มากเกินไป")
#     elif randomnum == secret:
#         print("ถูกต้อง!")
#         break
# print("โปรแกรมเสร็จสิน")


#โจทย์ที่ 8 : โปรแกรมคำนวณเกรด
# score = int(input("กรอกคะแนนของคุณ : "))
# if score >= 80:
#     print("GRADE A")
# elif score >= 70 and score <= 79:
#     print("GRADE B")
# elif score >= 60 and score <= 69:
#     print("GRADE C")
# elif score >= 50 and score <= 59:
#     print("GRADE D")
# else:
#     print("GRADE F")


#โจทย์ที่ 9 : หาจำนวนหลักของตัวเลข
# num = int(input("กรอกเลขของคุณ : "))
# count = 0

# while num>0:
#     count+=1
#     num//=10

# print(f"จำนวน {count} ครั้ง")


##โจทย์ที่ 10 (Mini Project) ระบบ ATM แบบง่าย
balance = int(input("กรุณากรอกเงินของคุณว่าเงินในบัญชีมีเท่าไหร่ : "))
while True:
    print("\n------เมนู------")
    print("1. ดูยอดเงิน")
    print("2. ฝากเงิน")
    print("3. ถอนเงิน")
    print("4. ออกจากโปรแกรม")

    menu = input("กรอกเลขเมนู : ")


    if menu == "1":
        print(f"ยอดเงินปัจจุบัน {balance}")
    elif menu == "2":
        amount = int(input("จำนวนเงินที่ฝาก : "))
        balance += amount
        print(f"ยอดเงินปัจจุบัน {balance}")
    elif menu == "3":
        amount = int(input("จำนวนเงินที่ถอน : "))

        if amount > balance:
            print("ยอดเงินไม่เพียงพอกรุณากรอกใหม่")
        else:
            balance -= amount
            print(f"ยอดเงินปัจจุบัน {balance}")

    elif menu == "4":
        print("ออกจากโปรแกรม")
        break
    else:
        print("ไม่มีอยู่ในเมนู กรุณาเลือกใหม่")