import datetime

user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

dealine_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
print(dealine_date)
datetime.datetime.today()