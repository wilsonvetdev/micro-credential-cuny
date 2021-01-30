# Python Version 3.9.x

print("---Lists Part 1 - Exercise One---")

courses = ['ET574', 'ET575', 'ET580', 'ET585', 'ET725']
courses_size = len(courses)

print(courses)
print(f"I am taking {courses_size} courses.")
print(courses[0])
print(courses[-1])

print("---Lists Part 1 - Exericse Two---")

numbers = []
numbers.append(2)
numbers.append(4)
print(numbers)
numbers += [0, 1, 3]
numbers.sort()
print(numbers)
numbers.append(5)
print(numbers)
print(numbers.pop(0))
print(numbers.pop(1))
print(numbers.pop(2))
print(numbers)

print("---Lists Part 1 - Exericse Three---")

letters = list(map(chr, range(97, 104)))
print(letters)
print(letters[-2])
letters.sort(reverse=True)
print(letters)
print(letters[-3])
b_index = letters.index("b")
letters[b_index] = "B"
print(letters)
d_index = letters.index("d")
letters[d_index] = "D"
print(letters)

temp = letters[0]
letters[0] = letters[-1]
letters[-1] = temp
print(letters)
letters.sort()
print(letters)

print("---Lists Part 2 - Exericse One---")

nums = [num for num in range(1, 11)]
print(nums)

for num in nums:
    print(f"{num} * 3 = {num * 3}")

print("---Lists Part 2 - Exericse Two---")
for num in nums:
    print(f"{num ** 2}")

print("---Lists Part 2 - Exericse Three---")
nums = [num for num in range(0, 51, 5)]

for num in nums:
    print(num)


print("---Lists Part 2 - Exericse Four---")

odd_numbers = [num for num in range(1, 21) if num % 2 != 0]
for num in odd_numbers:
    print(num)

print("---Lists Part 2 - Exericse Five---")

even_numbers = [num for num in range(0, 101, 2)]
print(even_numbers[0:5])
print(even_numbers[-6:])
print(even_numbers[10:16])