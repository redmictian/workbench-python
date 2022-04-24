calc_to_units = 24 * 60 * 60
unit_name = "seconds"


def days_to_units(num_of_days):
	return (f"{num_of_days} days are {num_of_days * calc_to_units} {unit_name}")

user_input = input("enter something\n")
my_var = days_to_units(int(user_input))
print(my_var)