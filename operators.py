a=30
b=9
# arithmetic operators
print("addition of twoo operators",a+b)
print("subtraction of two operators",a-b)
print("multiplication of two operators",a*b)
print("division of two operators",a/b)
print("remainder of two operators",a%b)
print("power of two operators",a**b) #exponetiation
print("modulo of two operators",a%b)
print("floor division of two operators",a//b)

# comparison operator

c=20
d=12

print(f"{c} and {d} are equal {c==d}")
print(f"{c} and {d} are not equal {c!=d}")
print(f"{c} is greater {d} :c>=d")
print(f"{c} is less {d} :c<d")

# logical operator
e=10
print(f"Is this statement true : {e>5 and e<10}")
print(f"is this statement true : {e>5 or e<10} ")
print(f"each statement is true the return false and viceversa : {not (e>5 or e<10)}")

#assignment operator

x = 5
x += 3  # Equivalent to: x = x + 3
print(x)  # Output: 8


x = 10
x -= 2  # Equivalent to: x = x - 2
print(x)  # Output: 8

x = 4
x *= 2  # Equivalent to: x = x * 2
print(x)  # Output: 8



x = 10
x /= 2  # Equivalent to: x = x / 2
print(x)  # Output: 5.0


x = 10
x %= 3  # Equivalent to: x = x % 3
print(x)  # Output: 1


x = 2
x **= 3  # Equivalent to: x = x ** 3
print(x)  # Output: 8


x = 10
x //= 3  # Equivalent to: x = x // 3
print(x)  # Output: 3


x = 6  # 6 = 110 in binary
x &= 3  # 3 = 011 in binary -> result: 010 = 2
print(x)  # Output: 2

x = 5  # 5 = 101 in binary
x |= 3  # 3 = 011 in binary -> result: 111 = 7
print(x)  # Output: 7

x = 5  # 5 = 101 in binary
x ^= 3  # 3 = 011 in binary -> result: 110 = 6
print(x)  # Output: 6

