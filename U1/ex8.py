n =input("Enter a number: ")


def inverse_num(n):
    if n == "":
        return ""
    else:
        return inverse_num(n[1:]) + n[0]

print(inverse_num(n))


