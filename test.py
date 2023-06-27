#This python code help you to teach your student about days!

days = []

num_day = int(input("How many days are there is a week? \n==>"))
if num_day == 7:
    print("")

else:
    print("are you sure",num_day,"days in the weeks")


for a in range(num_day):
    day = str(input("Enter the name of the day: "))
    days.append(day)

def day_print(day_name):
    for each_day in day_name:
        if isinstance(each_day, list):
            day_print(each_day)

        else:
            
            print("=>",each_day)

day_print(days)