
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
        # stops and breaks out at 3
        #break
        # continues through the list, but prints Found! at 3
        continue
    print(num)

# prints out each num in lest along with a, b or c to make all possible combinations
for num in nums:
    for letter in 'abc':
        print(num, letter)

x = 0

while x < 10:
    print(x)
    x += 1


def hello_func(greeting, name = 'You'):
    # pass is a place holder
    #pass
    # print('Hello Function.')
    #return 'Hello Function'
    return '{}, {}'.format(greeting, name)
 # prints out info on what is in the () while pass in in body
#print(hello_func())
#hello_func()
#print(hello_func().upper)
#print(hello_func('Hey', name = 'Claudia'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
#student_info('Math', 'Art', name='John', age=22)

# *, ** unpacks
student_info(*courses, **info)



# list[start:end:step] step allows for how many skips you want, default step prints out everything
# steps can be negative

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0  1  2  3  4  5  6  7  8  9
#         -10 -9 -8 7 -6 -5 -4 -3 -2 -1

#print(my_list[5:])
print(my_list[2:-1:2])


sample_url = 'http://get.vermeer.com'
print(sample_url)

# reverse string
print(sample_url[::-1])

# get the top level domain
print(sample_url[-4:])

# print the url without the http://
print(sample_url[7:])

# print the url without the http:// or the top level domain
print(sample_url[7:-4])


nums = [1,2,3,4,5,6,7,8,9,10]

# i want 'n' for each 'n' in nums
my_list = [n for n in nums]
print(my_list)

# i want 'n*n' for each 'n' in nums
# empty list to populate
my_list = []
# for loop to run through list
for n in nums:
    my_list.append(n*n)
print(my_list)
# OR
# all in 1 line of code, no for loop
my_list = [n*n for n in nums]
print(my_list)

# i want  'n' for each 'n' in nums if 'n' is even
my_list = []
for n in nums:
    if n%2 == 0:
        my_list.append(n)
print(my_list)
#OR
my_list = [n for n in nums if n%2 == 0]
print(my_list)

# i want a (letter, num) pair for each letter in 'abcd' and each number in 0123
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print(my_list)
# OR
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

# Dictionaries Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# i want a dict{'name': 'hero'} for eachname, hero in zip(names,heroes)
my_dict = {}
for name, hero in zip(names, heroes):
    my_dict[name] = hero
print(my_dict)
# OR
# if name is not Peter
my_dict = {name:hero for name, hero in zip(names, heroes) if name != 'Peter'}
print(my_dict)

# Set Comprehensions

# prints out each unique number
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)
#
my_set = {n for n in nums}
print(my_set)

# Generator Expressions
# i want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
     for n in nums:
         yield n*n

 my_gen = gen_func(nums)
#
my_gen = (n*n for n in nums)
for i in my_gen:
     print(i)

