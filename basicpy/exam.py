#Exam 1
# lst_score = list(map(int, input("กรอกเลข : ").split(",")))
# print(f"คะแนนรวม คือ {sum(lst_score)}")
# print(f"คะแนนเฉลี่ย คือ {(sum(lst_score) / len(lst_score))}")
# print(f"คะแนนสูงสุด คือ {max(lst_score)}")
# print(f"คะแนนน้อยสุด คือ {min(lst_score)}")

#==================================================================
#Exam 2
txt = input("กรอกข้อความ : ")

count = 0
for vowels in txt:
    if vowels.lower() in "aeiou":
        print(vowels)
        count += 1
    

print(f"มีจำนวนสระ {count}")


print(f"จำนวนตัวอักษรทั้งหมด คือ {len(txt)}")
