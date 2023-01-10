heights = [
    ["Jenny", 61], 
    ["Alexus", 70], 
    ["Sam", 67], 
    ["Grace", 64]]
# print(heights[-1])
heights.append(["Vik", 68])
# print(heights)

#A 2d list with three lists in each of the indices. 
tic_tac_toe = [
            ["X","O","X"], 
            ["O","X","O"], 
            ["O","O","X"]
]
# print(tic_tac_toe[1])

ages = [
    ["Aaron", 15],
    ["Dhruti", 16]
]

# Modifying 2D Lists
# In order to modify elements in a 2D list, an "index for the sublist" and the "index for the element of the 
# sublist" need to be provided. 
# The format for this is list[sublist_index][element_in_sublist_index] = new_value.
# A 2D list of names and hobbies
class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]

# The sublist of Jenny is at index 0. The hobby is at index 1 of the sublist. 
class_name_hobbies[0][1] = "Meditation"
# print(class_name_hobbies)

# Output
# [["Jenny", "Meditation"], ["Alexus", "Photography"], ["Grace", "Soccer"]]

class_name_hobbies[0][0] = "Abel" # Replace Jenny with Abel
# print(class_name_hobbies)

# output
# [['Abel', 'Meditation'], ['Alexus', 'Photography'], ['Grace', 'Soccer']]

class_name_hobbies[-1][-1] = "Hockey" # Replace "Soccer" with "Hockey"
# print(class_name_hobbies)

# output
# [['Abel', 'Meditation'], ['Alexus', 'Photography'], ['Grace', 'Hockey']]

# Accessing 2D Lists
# In order to access elements in a 2D list, an index for the sublist and the index for the element of the 
# sublist both need to be provided. The format for this is list[sublist_index][element_in_sublist_index].
class_name_test = [
    ["Jenny", 90],
    ["Alexus", 85.5],
    ["Sam", 83],
    ["Ellie", 101.5]
]
# print(class_name_test)
# Output
# [['Jenny', 90], ['Alexus', 85.5], ['Sam', 83], ['Ellie', '101.5']]

sams_score = class_name_test[2][1]
# print(sams_score)
# Output
# 83

ellies_score = class_name_test[-1][-1]
# print(ellies_score)
# Output
# 101.5

incoming_class = [
    ["Kenny", "American", 9],
    ["Tanya", "Ukrainian", 9],
    ["Madison", "Indian", 7]
]
# print(incoming_class)
# Output
# [['Kenny', 'American', 9], ['Tanya', 'Ukrainian', 9], ['Madison', 'Indian', 7]]

incoming_class[2][2] = 8
# print(incoming_class)
# Output
# [['Kenny', 'American', 9], ['Tanya', 'Ukrainian', 9], ['Madison', 'Indian', 8]]

incoming_class[-3][-3] = "Ken"
# print(incoming_class)
# Output
# [['Ken', 'American', 9], ['Tanya', 'Ukrainian', 9], ['Madison', 'Indian', 8]]

# List Method .remove()
# The .remove() method in Python is used to remove an element from a list by passing in the value of the element to be removed as an 
# argument. In the case where two or more elements in the list have the same value, the first occurrence of the element is removed.
# Example
my_list = ["Coffee", "water", "water", "soda", "water", "beer", "juice", "water"]
my_list.remove("water")# removes the first appearance of "water"
print(my_list)
# Output
# ['Coffee', 'water', 'soda', 'water', 'beer', 'juice', 'water']