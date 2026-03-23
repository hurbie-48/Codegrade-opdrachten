user_input = input("Geef een lijst met nummers (gescheiden door komma's) ")
number_list = user_input.split(",")
number_list_int = []
for number in number_list:
    number_list_int.append(int(number))
# Print the total number of items in the list.
print(len(number_list_int))
# Print the last item in the list.
print(number_list_int[-1])
# Print the list in reverse order.
print(number_list_int[::-1])
# Print Yes if the list contains a 5 and No otherwise.
if 5 in number_list_int:
    print("Yes")
else:
    print("No")
# Print the number of fives in the list.
print(number_list_int.count(5))
# Remove the first and last items from the list, sort the remaining items, and print the result.
number_list_int.pop(0)
number_list_int.pop(-1)
number_list_int.sort()
print(number_list_int)
# Print how many integers in the list are less than 5. 
smaller_than_five = []
for number in number_list_int:
    if number < 5:
        smaller_than_five.append(number)
print(len(smaller_than_five))