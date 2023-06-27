#This python code help you to teach your student about days!

days = []

num_day = int(input("How many days are there is a week? \n==>"))
if num_day == 7:
    print("")

else:
    print("Are you sure where are",num_day,"days in the week!")


for a in range(num_day):
    day = str(input("What are they: "))
    days.append(day)

def day_print(day_name):
    for each_day in day_name:
        if isinstance(each_day, list):
            day_print(each_day)

        else:
            
            print(">",each_day)
print("\n\nThe days are: ")
day_print(days)