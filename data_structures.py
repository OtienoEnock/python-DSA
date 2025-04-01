# create an empty list. Append elements to my_list
my_list = []

my_list. append(10)
my_list. append(20)
my_list. append(30)
my_list. append(40)

# Insert 15 into second position. Extend my_list with another 

my_list.insert(1, 15)

new_list = [50, 60, 70]
my_list.extend(new_list)

#remove last element, sort ascending, and print index of 30. 
my_list.pop()
my_list.sort(reverse = False)
print(my_list.index(30))
