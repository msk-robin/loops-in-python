# THIS IS LOOPS EXAMPLES:
# 1 set initial value
# 2 loop through the number
# 3 update changes

# for number in range(1,11):
#      total = 0          # total gets re-assigned 0 every time the loop body runs
#      total += number

# print(total) # 10   <- WRONG!
# Find the sum of the even numbers from 10 to 100 (including 10 and 
# even = 0
# for num in range(10,101):
#   if (num % 2 == 0):
#     even+=1
# print(even)    

# for number in range(1, 10):
#     if(number % 2 != 0):
#         print(number)

numbers = [68,12,32,70,-4,0,-13,13,86,91,-79,]

smallest = numbers[0]

for i in numbers:
    if i < smallest:
        smallest = i
print(smallest)        
 
 