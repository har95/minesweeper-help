
import random
real_field= [0,0,0,0,0]  # field of numbers where the ine is inserted
mine_a = 2
mine_list =[]  # location of mines list
while mine_a != 0:
    mine_location = random.randint(0, real_field.count(0) - 1)  # puts mine into the field
    mine_list.append(mine_location)  # puts location of mine into a list
    real_field[mine_location] = '*'
    mine_a -= 1  # loops the while until all mines are in list
mine_list = mine_list *2 # doubles mine list
for bomb in mine_list:  # part I need help with taking the mine location and adding one to the left and one to the right
    bomb = mine_list[1]
    bomb += 1
for name in real_field: # removes formatting for the list
    print(name, '', end=' ')
print(mine_list)  # prints mine location list to show if for loop works right
