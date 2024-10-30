height = int(input("Height: "))
root = height-1

for i in range(0, height * 2, 2):
    print(" " * height, end="")
    height -= 1
    print('x' * (i + 1))

print(" " * root + "| |")