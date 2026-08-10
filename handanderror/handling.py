##Read text file##
#ข้อที่ 1 
# file = open("score.txt")

# # print(file.readline()) #อ่านข้อมูลทีละบรรทัด (บรรทัดที่ 1)
# # print(file.readline()) #อ่านบรรทัดที่ 2

# # for sc in file: #อ่านค่าทั้งหมด ทุกบรรทัด
# #       print(sc)

# #ทำเป็นเงื่อนไขเล็กๆ เช่น คนไหนมีคะแนนเป็นเลขคู่ให้นับ 1
# even_count = 0 
# for i in file:
#     score_int = int(i) #เป็น Type จาก String เป็น Integer
#     if score_int % 2 == 0: #ถ้าหาร 2 ลงตัว
#         even_count += 1 #ให้นับ 1 

# print(f"Student with even-numbers score = {str(even_count)}")

# file.close()
#------------------------------------------------------------------------

#ข้อที่ 2
# file = open("group_scores.txt")

# pass_count = 0

# for gropu_scores in file: #รอบแรกจะได้เป็น String ก็คือ "87 22 34 51 70 ........."
#     gropu_scores_lst = gropu_scores.split(" ") #ก็คือการแยกคำ ระหว่างช่องว่าง แล้วเป็นค่า list
#     for score in gropu_scores_lst:
#         score_int = int(score)
#         if score_int >= 50:
#             pass_count += 1

# print(f"Student passed = {str(pass_count)}") #ส่งค่าออกเป็น String


# file.close()
#------------------------------------------------------------------------
#การเขียนแบบ With Statement
# with open("test.txt", "r", encoding="utf-8") as file_read:
#     print(file_read.read())
#------------------------------------------------------------------------


##Write text file##
#ไม่ต้องไปสร้างไฟล์เอง เดี๋ยวมันจะสร้างขึ้นมาให้
# file_read = open("group_scores.txt")
# file_write = open("test.txt", "w")

# # สร้างคำที่จะเขียนลงในไฟล์
# # file.write("ไก่จ๋า ")
# # file.write("ได้ยินมั้ยว่าเสียงใคร ")
# # file.write("อิอิ")

# for group_score in file_read: #อ่านค่าตัวเลขจากไฟล์ group_scores
#     sum_score = 0
#     group_score_lst = group_score.split(" ") #แยก ทำเป็น list
#     for score in group_score_lst: 
#         score_int = int(score)
#         sum_score += score_int

#     avg_score = sum_score / len(group_score_lst)
#     file_write.write(str(avg_score) + "\n")
 

# file_read.close()
# file_write.close()

#การเขียนแบบ With Statement
# with open("test.txt", "w", encoding = "utf-8") as file_write:
#     file_write.write("ไก่จ๋า ")
#     file_write.write("ได้ยินมั้ยว่าเสียงใคร ")
#     file_write.write("กุ๊กกุ๊ก ")
#------------------------------------------------------------------------

##Read + Write##
#แบบทั้งอ่าน และเขียน
# with open("group_scores.txt", "r", encoding="utf-8") as file_read, \
#      open("test.txt", "w", encoding="utf-8") as file_write:
#         for group_score in file_read: #อ่านค่าจากไฟล์ group_scores.txt แล้วเก็บลงใน group_score
#             group_score_lst = list(map(int, group_score.split(" "))) #แปลง group_score เป็น int แล้วเก็บลงใน list

#             avg_score = sum(group_score_lst) / len(group_score_lst)
#             file_write.write(str(avg_score) + "\n")

# print("ทำการเพิ่มสำเร็จ")


#ข้อที่ 2 แบบข้อความไม่คำนวณ จากการอ่านไฟล์ แล้วไปเขียนอีกไฟล์ 
# with open("score.txt", "r", encoding="utf-8") as file_read, \
#      open("test.txt", "w", encoding="utf-8") as file_write:
     
#      file_write.write(file_read.read())

# print("สำเร็จ")
#------------------------------------------------------------------------

#โจทย์ 1 รับค่าจากผู้ใช้แล้วบันทึกลงไฟล์ txt
# with open("test.txt", "a", encoding="utf-8") as file_write:
#     note = input("กรอกข้อความ : ")
#     file_write.write(note) 
#     print("เพิ่มลงในไฟลล์แล้ว")

#โจทย์ 2 อ่านค่าจากไฟล์
# with open("test.txt", "r", encoding="utf-8") as file_read:
#     print(file_read.read())

#โจทย์ 3 ทำเป็น Note App
# def add_note():
#     with open("test.txt", "a", encoding="utf-8") as file:
#         note = input("กรอกข้อความที่จะเพิ่ม : ")
#         file.write(note + "\n")
#         print("เพิ่มข้อความสำเร็จ")

# def show_note():
#     with open("test.txt", "r", encoding="utf-8") as file:
#         print(file.read())

# while True:
#     print("\n------เมนู------")
#     print("1. เพิ่มข้อความ")
#     print("2. ดูข้อความ")
#     print("3. ออก")

#     choice = input("เลือกเมนู : ")

#     if choice == "1":
#         add_note()

#     elif choice == "2":
#         show_note()

#     elif choice == "3":
#         print("ออกจากโปรแกรม")
#         break
#------------------------------------------------------------------------

#Mini project เก็บข้อมูลนักเรียน
def add_stdent():
     
    name = input("กรอกชื่อที่จะเพิ่ม : ")
    score = float(input("กรอกคะแนนจะเพิ่ม : "))
    age = int(input("กรอกอายุเพิ่ม : "))

    with open("test.txt", "w", encoding="utf-8") as file:
        file.write(f"{name}, {score}, {age}\n")
        
    print("เพิ่มข้อมูลเรียบร้อย")

def show_student():
    with open("test.txt", "r", encoding="utf-8") as file:
        for line in file:
            name, score, age = line.strip().split(",") #split(",") คือ การแปลงเป็น string โดยตัดจากตัว (,) แบ่งใน list 

        print(f"name : {name}")
        print(f"score : {score}")
        print(f"age : {age}")

while True:
    print("\n------เมนู------")
    print("1. เพิ่มนักเรียนลงไฟล์")
    print("2. ดูนักเรียนในไฟล์")
    print("3. ออกจากโปรแกรม")

    choice = input("เลือกเมนู : ")

    if choice == "1":
        add_stdent()

    elif choice == "2":
        show_student()

    elif choice == "3":
        print("ออกจากโปรแกรม")
        break

    else:
        print("กรุณาเลือกเมนูใหม่")


#------------------------------------------------------------------------

# lst = [10,20,30,40,50]
# print(" | ".join(map(str, lst))) #join แทรกระหว่าง ค่า