import sys

def find_possible_moves():
    print("hi")

#Open files and store contents in variable
file = open(sys.argv[1], 'r')
matrix = [[],[],[]]
for i in range(3):
    string = file.readline()
    for char in string:
        if(char.isnumeric()):
            matrix[i].append(int(char))
print(matrix)
file.close()

#A* Search
#g(n) = number of tiles misplaced
#d = depth of state
count = 0
counter = 1
for row in len(matrix):
    for col in len(matrix[row]):
        if(matrix[row][col] != counter):
            count += 1
print("Count = " + count)

finished_nums = [[1,2,3],[4,5,6],[7,8,0]]

#Save goal file
# goal_nums = start_nums
# goal_string = ""
# count = 0
# for i in range(3):
#     for j in range(3):
#         goal_string += str(goal_nums[count]) +" "
#         count += 1
#     goal_string += "\n"
# goal_string += "END OF FILE"
# print("goal string :\n" + goal_string)

# goal_file = open(sys.argv[2], "a")
# goal_file.write(goal_string)
# goal_file.close()