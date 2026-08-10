##01
# with open("stdin", "r") as f:
#     data = f.read()

# inputs = data.split() if len(data) else []

# # inputs is a list of strings
# # write your code below
# nums = list(map(int, inputs))

# target = nums[-1]
# A = nums[:-1]

# found = False

# for i in range(len(A)):
#     for j in range(i + 1, len(A)):
#         if A[i] + A[j] == target:
#             print(i, j)
#             found = True
#             break
#     if found:
#         break

# if not found:
#     print(-1, -1)
## ==========================================================

##02
# with open("stdin", "r") as f:
#     data = f.read()

# inputs = data.split() if len(data) else []

# # inputs is a list of strings
# # write your code below

# nums = list(map(int, inputs))

# points = []
# for i in range(0, len(nums), 2):
#     points.append((nums[i], nums[i + 1]))

# minDistance = float("inf")
# index1 = -1
# index2 = -1

# for i in range(len(points)):
#     for j in range(i + 1, len(points)):
#         x1, y1 = points[i]
#         x2, y2 = points[j]

#         distance = (x2 - x1) ** 2 + (y2 - y1) ** 2

#         if distance < minDistance:
#             minDistance = distance
#             index1 = i
#             index2 = j

# print(index1, index2)
## ==========================================================

##03
with open("stdin", "r") as f:
    data = f.read()

inputs = data.split() if len(data) else []

# inputs is a list of strings
# write your code below

text, pattern = data.strip().split("|")

found = False

for i in range(len(text) - len(pattern) + 1):
    match = True

    for j in range(len(pattern)):
        if text[i + j] != pattern[j]:
            match = False
            break

    if match:
        print(i, end=" ")
        found = True

if not found:
    print(-1)