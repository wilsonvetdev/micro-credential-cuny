# Python Version 3.9.x

print("---Exercise One---")

first_name = "Wilson"
last_name = "Ng"
id = 321545

print(
f"""Hi {first_name}, Welcome to QCC!

name: {first_name} {last_name} id: {id}

Spring 2021 Classes:
ET574 ET575 MA471 ET725
""")

print("---Exercise Two---")

n = 2 
counter = 1 

while counter <= 10:
    print(f"{n} * {counter} = {n * counter}")
    counter += 1

print("")
print("---Exercise Three---")

n = 10
d = 3

print(int(10 / 3))
print("%.4f" % ((10 / 3) % 1))
print(10 % 3)