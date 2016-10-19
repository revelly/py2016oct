#passin a dict by value
def pop(ax, key):
    x.pop(key)

a={"HYD":"TG", "CHE":"TN", "BLR":"KA"}
print(a)
pop(a.copy(), "HYD")
print(a)
