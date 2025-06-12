rainfall=[10,20,41,21,34,11,20]
location="raichur"

def print_rainfall(values):
    day=1
    for value in values:
        print("day", day,":", value)
        day+=1
def avg_rainfall(values):
    import math
    return math.fsum(values)/len(values)
def change_location(new_loc):
    global location
    location=new_loc
    print("the new locatio is", location)

print_rainfall(rainfall)
print(avg_rainfall(rainfall))
print(location)
change_location("banglore")
print(location)