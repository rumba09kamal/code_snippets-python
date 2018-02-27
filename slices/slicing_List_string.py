import sys
print(sys.version)
print(sys.executable)

#refer --> https://docs.python.org/2.3/whatsnew/section-slices.html

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#               0,   1,    2,  3,  4,   5,  6,  7,  8, 9 ==> positive index
#              -9,  -8,  -7, -6, -5, -4, -3, -2, -1 ==> negative index

# syntax
###### list[start:end:step] ###########
#  end--> non-inclusive

print my_list[3]  # prints value

print my_list[0:10]
print my_list[0:-1]
print my_list[:-1]
print my_list[::]
print my_list[-9:10]

print my_list[::-1]  # reverse the list
print my_list[2:-1:2]


### slicing the sting ######
url = 'https://kalampost.com'

# reverse the url
print url[::-1]

# print only the top level domain(ie. `.com`)
print url[-4:]

# print without `https`
print url[8:]

# print url withour `https` or top level domain
print url[8:-4]
