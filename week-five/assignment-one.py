# Python 3.9.1

# Wilson Ng - Week Five Assignment One - 02/01/2021

print("---Exercise One---")
print(" ")
num = -41 # update this number appropriately for exercises

if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by 5")
    print(f"{num} is divisible by 3")

print(" ")
print("---Exercise Two---")
print(" ")

if num % 4 == 0:
    print(f"{num} is divisible by 4")
elif num % 2 == 0:
    print(f"{num} is divisible by 2")
elif num % 4 != 0 or num % 2 != 0:
    print(f"{num} is not divisible by 2 or 4")

print(" ")
print("---Exercise Three---")
print(" ")

if num % 2 == 0 and num > 50:
    print(f"{num} is a positive even integer greater than 50")
elif num < 0 and num % 2 != 0:
    print(f"{num} is a negative odd integer")

print(" ")
print("---Exercise Four---")
print(" ")

average = 60

if average in range(90, 101):
    print("A")
elif average in range(80, 91):
    print("B")
elif average in range(70, 81):
    print("C")
elif average in range(60, 71):
    print("D")
elif average < 60:
    print("F")

print(" ")
print("---Exercise Five---")
print(" ")

grades = [73, 63, 80, 43, 90, 56]
print("Grade Average:", sum(grades) / len(grades))

print(" ")
print("---Exercise Six---")
print(" ")

vehicles = [ "car", "Truck", "boat", "PLANE"]
e = "truck"

for i in range(len(vehicles)):
    if e == vehicles[i].lower():
        print(f"{vehicles[i]} is in position 1.")

print(" ")
print("---Exercise Seven---")
print(" ")

students = ["Jim", "Jane", "John", "Joe", "Jack", "Jill", "Joan"]

tutors = ["Jane", "Joe", "Jill"]

print("Students that are tutors:")
for tutor in tutors:
    if tutor in students:
        print(f"{tutor}")

print(" ")
print("---Exercise Eight---")
print(" ")

nums = [num for num in range(1, 21)]
printEvens = False
printOdds = False
nums_str = ""

for num in nums:
    if printEvens and num % 2 == 0:
        nums_str += str(num) + " "
    elif printOdds and num % 2 != 0:
        nums_str += str(num) + " "
    elif printEvens and printOdds:
        nums_str += str(num) + " "

print(nums_str)


print(" ")
print("---Exercise Nine---")
print(" ")

numbers = [num for num in range(1, 31)]
numbers_str = ""

print(" ".join(str(number) for number in numbers if number % 3 == 0 or number % 5 == 0))
print(" ".join(str(number) for number in numbers if number % 3 == 0))
print(" ".join(str(number) for number in numbers if number % 3 != 0 and number % 5 != 0))

print(" ")
print("---Exercise Ten---")
print(" ")

grades = [83, 80, 65, 75]
weights = [1, 1, 1, 1.5]

print("Minimum Grade Dropped:", grades.pop(grades.index(min(grades)))) # drops minimum grade and print to console

total = 0
for i in range(len(grades)):
    total += grades[i] * weights[i+1]

weighted_average = total / len(grades)

print("Total:", total)
print("Weighted Average: %.2f" % weighted_average )
