import math

a = 10
print("Integer:", a)
print("Type:", type(a))
print("Addition:", a + 5)
print("Square:", a ** 2)

b = 12.5
print("\nFloat:", b)
print("Type:", type(b))
print("Division:", b / 2)
print("Rounded:", round(b))


c = 3 + 4j
print("\nComplex:", c)
print("Type:", type(c))
print("Real part:", c.real)
print("Imaginary part:", c.imag)
print("Conjugate:", c.conjugate())


s = "Python"
print("\nString:", s)
print("Type:", type(s))
print("Length:", len(s))
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("First character:", s[0])
print("Slicing:", s[0:3])


lst = [10, 20, 30, 40, 50]
print("\nList:", lst)
lst.append(60)
print("After append:", lst)
print("Length:", len(lst))
print("Maximum:", max(lst))
print("Minimum:", min(lst))
print("Sum:", sum(lst))


t = (10, 20, 30, 40)
print("\nTuple:", t)
print("Type:", type(t))
print("First element:", t[0])
print("Length:", len(t))
print("Maximum:", max(t))


student = {
    "name": "Rahul",
    "age": 20,
    "marks": 85
}

print("\nDictionary:", student)
print("Name:", student["name"])
print("Keys:", student.keys())
print("Values:", student.values())


numbers = {1, 2, 3, 4, 5}
print("\nSet:", numbers)
numbers.add(6)
print("After adding:", numbers)
print("Length:", len(numbers))


fs = frozenset([1, 2, 3, 4])
print("\nFrozenset:", fs)
print("Type:", type(fs))


x = True
y = False
print("\nBoolean:", x)
print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)


z = None
print("\nNone:", z)
print("Type:", type(z))


print("sqrt(25):", math.sqrt(25))
print("power:", math.pow(2, 3))
print("factorial:", math.factorial(5))
print("ceil:", math.ceil(4.2))
print("floor:", math.floor(4.8))
print("sin(90 degrees):", math.sin(math.radians(90)))
print("cos(0 degrees):", math.cos(math.radians(0)))
print("log(10):", math.log(10))
print("Pi:", math.pi)
