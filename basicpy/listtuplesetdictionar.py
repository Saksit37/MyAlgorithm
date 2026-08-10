##List##
#ข้อที่ 1
# friuts = ["Apple, Banana, Orage"]
# print(friuts)
#---------------------------------------------------------------------------

#ข้อที่ 2
# numbers = [10, 20, 30, 40, 50]
# print(numbers[0], numbers[-1]), print(sorted(numbers))
#---------------------------------------------------------------------------

#ข้อที่ 3 รับจำนวนจากผู้ใช้ และแสดงรายชื่อทั้งหมด
# roundnm = int(input("กรุณาระบุจำนวนรอบ : "))
# name1 = []

# for _ in range(roundnm):
#     name0 = input("กรุณากรอกชื่อ : ")
#     name1.append(name0)

# for i in name1:
#     print(i)
#---------------------------------------------------------------------------

#ข้อที่ 4
# num = list(map(int, input("กรุณากรอกเลข : ").split(","))) #map(int, (.....)) คือการเปลี่ยนทุกตัวเป็น int
# # lst = list(num)
# for i in num:
#     print(i)

# print(f"\nผลรวม คือ {sum(num)}")
# print(f"เลขที่มากที่สุด คือ {max(num)}")
# print(f"เลขที่น้อยที่สุด คือ {min(num)}")
#---------------------------------------------------------------------------

#ข้อที่ 5 Mini project
# def add_product(products):
#     addProduct = input("ชื่อสินค้าที่จะเพิ่ม : ")
#     products.append(addProduct)

# def show_product(products):
#     for i, item in enumerate(products, start=1):
#         print(f"{i}. {item}")

# def remove_product(products):
#     removeProduct = input("ชื่อสินค้าที่จะลบ : ")

#     if removeProduct in products:
#         products.remove(removeProduct)

# product = []
# while True:
#     print("------เมนู------")
#     print("1. เพิ่มสินค้า")
#     print("2. ดูสินค้า")
#     print("3. ลบสินค้า")
#     print("4. ออกจากโปรแกรม")

#     choice = input("กรุณาเลือกเมนู : ")

#     if choice == "1":
#         add_product(product)
#         print("เพิ่มสินค้าเรียบร้อย")
    
#     elif choice == "2":
#         show_product(product)

#     elif choice == "3":
#         remove_product(product)
#         print("ลบสินค้าเรียบร้อย")

#     elif choice == "4":
#         print("ออกจากโปรแกรม")
#         break

#     else:
#         print("กรุณาเลือกเมนูที่แสดง")
#---------------------------------------------------------------------------

#ด่านที่ 2 List + Function 
#ข้อที่ 6 อ่านค่าใน list แล้วแสดงทีละตัว
# def show_fruits(items):
#     for i in items:
#         print(i)

# item = ["Apple", "Banana", "Orange"]
# show_fruits(item)
#---------------------------------------------------------------------------

#ข้อที่ 7 คืนค่าผลรวม
#แบบตรงตัว
# def get_total(numbers):
#     sum = 0
#     for i in numbers:
#         sum += i
#     return sum

# lst = list(map(int, input(": ").split(",")))
# print(get_total(lst))

#แบบสั้นๆ
# def get_total(numbers):
#     return sum(numbers)

# lst = list(map(int, input("กรอกเลขที่จะหาผลรวม : ").split(",")))
# print(get_total(lst))
#---------------------------------------------------------------------------

#ข้อที่ 8 หาค่ามากที่สุดโดยห้ามใช้ max
# def get_max(nums):
#     nums = sorted(nums)
#     return nums[-1]

# num0 = list(map(int, input("กรอกเลข : ").split(",")))
# print(get_max(num0))
#---------------------------------------------------------------------------

#ด่านที่ 3 List menu Program
#ข้อที่ 9 ปรับปรุงโปรแกรมสินค้า
##แบบ No Function##
# lst1 = []
# while True:
#     print("------เมนู------")
#     print("1. เพิ่มสินค้า")
#     print("2. ดูสินค้า")
#     print("3. ลบสินค้า")
#     print("4. ดูจำนวนสินค้า")
#     print("5. ออกโปรแกรม")

#     choice = input("เลือกเมนู : ")

#     if choice == "1":
#         product = input("กรอกชื่อสินค้าที่จะเพิ่ม : ")
#         lst1.append(product)
#         print(f"เพิ่มสินค้า {product} เรียบร้อย ")
    
#     elif choice == "2":
#         for i,j in enumerate(lst1, start=1):
#             print(f"{i}. {j}")

#     elif choice == "3":
#         product_rm = input("กรอกชื่อสินค้าที่จะลบ : ")
#         if product_rm in lst1:
#             lst1.remove(product_rm)
#             print(f"ลบสินค้า {product_rm} เรียบร้อย")

#     elif choice == "4":
#         print(f"มีจำนวนทั้งหมด {len(lst1)} รายการ")

#     elif choice == "5":
#         print("ออกจากโปรแกรม")
#         break

#     else:
#         print("กรุณากรอกให้ตรงกับเมนู")

##แบบ Function##------------------------------------
# def add_product(products):
#     prod = input("กรอกชื่อสินค้าที่จะเพิ่ม : ")
#     products.append(prod)
#     return prod

# def show_product(products):
#     for i,j in enumerate(products, start=1):
#         print(f"{i}. {j}")

# def remove_product(products):
#     prod = input("กรอกชื่อสินค้าที่จะลบ : ")
#     if prod in products:
#         products.remove(prod)

# def quantity_product(products):
#     return len(products)

# product = []
# while True:
#     print("------เมนู------")
#     print("1. เพิ่มสินค้า")
#     print("2. ดูสินค้า")
#     print("3. ลบสินค้า")
#     print("4. ดูจำนวนสินค้า")
#     print("5. ออกโปรแกรม")

#     choice = input("เลือกเมนู : ")

#     if choice == "1":
#         product_name = add_product(product)
#         print(f"เพิ่มสินค้าที่ชื่อ {product_name} เรียบร้อย")

#     elif choice == "2":
#         show_product(product)

#     elif choice == "3":
#         remove_product(product)
#         print(f"ลบสินค้าเรียบร้อย")      

#     elif choice == "4":
#         quantity_product(product)
#         print(f"มีจำนวนทั้งหมด {len(product)} เรียบร้อย")
    
#     elif choice == "5":
#         print("ออกจากโปรแกรม")
#         break

#     else:
#         print("ช่วยเลือกให้ตรงกับเมนูที่กำหนด")
#---------------------------------------------------------------------------

#ด่านที่ 4 Nested Loop + List
#ตารางแม่สูตรคูณ
#ข้อที่ 11
# def calculationtable(num):
#     for i in range(1, 13):
#         print(f"{i} x {num} = {i*num}")

# n1 = int(input("กรอกเลข : "))
# calculationtable(n1)
#---------------------------------------------------------------------------

#ข้อที่ 12
# def all_score(score):
#      for i,j in enumerate(score, start=1):
#          print(f"คนที่ {i} ได้ {j} คะแนน")

# def add_score(score):
#     sce = float(input("กรอกคะแนนเพิ่ม : "))
#     score.append(sce)

# def average_score(score):
#      return sum(score) / len(score)

# def max_score(score):
#     # แบบเต็ม
# #     soe = sorted(score)
# #     return soe[-1]

# # score = list(map(int, input("กรอกเลข : ").split(",")))
# # print(max_score(score))
#     return max(score)

# def min_score(score):
#     return min(score)

# lst1 = list(map(float, input("กรอกคะแนน : ").split(",")))
# print("-"*40)

# while True:
#     print("------เมนู------")
#     print("1. ดูคะแนนทั้งหมด")
#     print("2. เพิ่มคะแนน")
#     print("3. คำนวณค่าเฉลี่ย")
#     print("4. หาคะแนนสูงสุด")
#     print("5. หาคะแนนต่ำสุด")
#     print("6. ออกโปรแกรม")

#     choice = input("เลือกเมนู : ")

#     if choice == "1":
#         all_score(lst1)

#     elif choice == "2":
#         add_score(lst1)
#         print("เพิ่มคะแนนเรียบร้อน")

#     elif choice == "3":
#         print(f"ค่าเฉลี่ย คือ {average_score(lst1):.2f} คะแนน")

#     elif choice == "4":
#         print(f"คะแนนมากที่สุด คือ ได้ {max_score(lst1)} คะแนน")

#     elif choice == "5":
#         print(f"คะแนนน้อยที่สุด คือ ได้ {min_score(lst1)} คะแนน")
    
#     elif choice == "6":
#         print("ออกจากโปรแกรม")
#         break

#     else:
#         print("กรุณาเลือกให้ตรงกับเมนู")
#---------------------------------------------------------------------------

##Dictionary##
# colors = {
#     "red" : "แดง",
#     "blue" : "น้ำเงิน",
#     "green" : "เขียว"
# }
# colors["yellow"] = "เหลือง" #เพิ่มข้อมูล
# colors["blue"] = "คราม" #แก้ไขข้อมูล

# print(colors.keys()) #ดึงรายชื่อ key ทั้งหมด
# print(colors.values()) #ดึงข้อมูลมา
# print(colors.items()) #ดึงทั้ง key และ value

# for key in colors.keys(): #loop เอาแค่ key
#     print(key)

# for value in colors.values(): #loop เอาแค่ value
#     print(value)

# for key, value in colors.items(): #loop แสดง key และ value
#     print(key, "= ", value)

# colors.pop("blue") # ลบสีน้ำเงิน
# colors.clear() # ลบข้อมูลทั้งหมด

# print(len(colors)) #ดูจำนวนใน Dictionary
# print(colors) #ส่งค่าออกทั้ง colors
#---------------------------------------------------------------------------

#ข้อที่ 1 #แสดงข้อมูลทั้งหมด
# student = {
#     "name" : "Sakai",
#     "score" : 95
# }
# for key, value in student.items():
#     print(key, "= ", value)
#---------------------------------------------------------------------------

#ข้อที่ 2
# name = input("กรอกชื่อ : ")
# score = float(input("กรอกคะแนน : "))
# age = int(input("กรอกอายุ : "))

# lst = 

# student = {
#     "name" : name,
#     "score" : score
# }
# student["age"] = age

# lst.append(student)

# # for k, v in student.items():
# #    print(f"{k} : {v}")

# print(f"ชื่อ : {student['name']}") #แบบดึงข้อมูลตรงตัว
# print(f"คะแนน : {student['score']} คะแนน") #แบบดึงข้อมูลตรงตัว
# print(f"อายุ : {student['age']} ปี")

# for i, j in enumerate(lst, start=1):
#     print(f"{i}. {j}")
#---------------------------------------------------------------------------

##Mini Profect##
#เพิ่มรายชื่อ
def addstd():

    name = input("กรอกชื่อ : ")
    if name == "0":
        return
    
    score = input("กรอกคะแนน : ")
    if score == "0":
        return
    
    age = input("กรอกอายุ : ")
    if age == "0":
        return

    return {
        "name" : name,
        "score" : float(score),
        "age" : int(age)
    }

#ดูรายชื่อ
def showstd(students):
    for i, j in enumerate(students, start=1):
        print(f"\nคนที่ {i}")
        for k, v in j.items():
            print(f"{k} : {v}")

# ลบรายชื่อ
def dlstd(students):
    name = input("กรอกชื่อที่ต้องการจะลบ : ")
    
    if name == "0":
        return

    for student in students:
        if student["name"] == name: #ถ้า ชื่อ ที่ส่งเข้ามามันเหมือนกันที่พิมเข้ามา ให้เข้าฟังก์ชั่น
            students.remove(student)
            print("ลบข้อมูลเรียบร้อย")
            return
        
    print("ไม่พบข้อมูล")

# แก้ไขรายชื่อ
def  updatestd(students):
        
        name = input("กรอกชื่อที่ต้องการจะแก้ไข : ")

        if name == "0":
            return

        for student in students:
            
            if student["name"] == name:

                print("\n1. เปลี่ยนรายชื่อ")
                print("2. เปลี่ยนคะแนน")
                print("3. เปลี่ยนอายุ")

                choice = input("เลือกเมนู : ")

                if choice == "1":
                    student["name"] = input("กรอกชื่อใหม่ : ")
                
                elif choice == "2":
                    student["score"] = float(input("กรอกคะแนนใหม่ : "))

                elif choice == "3":
                    student["age"] = int(input("กรอกอายุใหม่ : "))

                print("แก้ไขเรียบร้อย")
                return
            
        print("ไม่พบข้อมูล")


# ค้นหานักเรียน
def findstd(students):
    name = input("กรอกชื่อที่จะค้นหา : ")

    if name == "0":
        return
    
    for student in students:
        
        if student["name"] == name:

            for k, v in student.items():
                print(f"{k} : {v}")    
            
            return
        
    print("ไม่พบข้อมูล")


students = []
while True:
    print("\n------เมนู------")
    print("1. เพิ่มชื่อนักเรียน")
    print("2. ดูชื่อนักเรียน")
    print("3. ลบชื่อนักเรียน")
    print("4. แก้ไขข้อมูล")
    print("5. ค้นหาข้อมูล")
    print("6. ออกจากโปรแกรม")

    choice = input("เลือกเมนู : ")

    if choice == "1":
        #student = addstd()
        if student := addstd(): #คือ student = addstd()
            students.append(student)
            print("เพิ่มข้อมูลเรียบร้อย")
        else:
            print("ย้อนกลับแลล้ว")
            
    elif choice == "2":
        showstd(students)

    elif choice == "3":
        dlstd(students)

    elif choice == "4":
        updatestd(students)

    elif choice == "5":
        findstd(students)

    elif choice == "6":
        print("ออกจากโปรแกรม")
        break

    else:
        print("เลือกให้ตรงกับเมนู")