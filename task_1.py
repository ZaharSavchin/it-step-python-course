def division(a, b):
    try:
        return round((a*b)**0.5, 3)
    except Exception as err:
        return f"error: {err}"


print(division(7, "3"))
print(division(7, 2))



