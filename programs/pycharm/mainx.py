arr = range(5)
print arr
arr.insert(5, 5)
print arr
arr.insert(100, 6)
print arr


print
arr = [10, 11, 12, 13, 14, 15]
for i in range(len(arr)):
    print arr[i],

print
for i in reversed(range(len(arr))):
    print arr[i],

print
for i in range(len(arr)-1, -1, -1):
    print arr[i],

print
for i in range(len(arr))[::-1]:
    print arr[i],

print
for i, val in enumerate(arr):
    print i, val



print
print
arr = [None]*5
print arr
arr[1] = 9
print arr


print
arr = [1,1,2,3,4,4,4,5,5]
print arr
arr.remove(min(arr))
print arr
arr.remove(min(arr))
print arr
arr.remove(min(arr))
print arr
arr.remove(min(arr))
print arr
arr.remove(min(arr))
print arr
arr.remove(min(arr))
print arr
arr.remove(min(arr))
print arr
arr.remove(min(arr))
print arr

arr = range(10)
for i in range(len(arr)):
    print i,
    print arr[i],
    i += 2
    print i

arr = "supratik"
print arr
print arr[::1]
print arr[::2]
print arr[::-1]
print arr[-1]
print arr[-2]



print
document = "Practice makes   perfect "
words = document.split()
print words
words = document.split(' ')
print words
words = document.split(' ', 4)
print words


print
row = [0]*3
print row
matrix = []
for i in range(3):
    matrix.append(row)
print matrix

matrix = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
print matrix, len(matrix), len(matrix[0])
for row in matrix:
    for col in row:
        print col,
    print

print
hasht = {}
print hasht.get("abc")
hasht["abc"] = 3
print hasht.get("abc")
print hasht["abc"]
hasht["def"] = 4

for idx, key in enumerate(hasht):
    print idx, key, hasht[key]
for key in hasht:
    print key, hasht[key]


ar1 = ['a', 'b', 'c', 'd']
ar2 = ar1[:]
ar2[2] = 'z'
print ar1
print ar2

st1 = "abcd"
st2 = st1 + "xyz"


flt = float(5)/float(2)
print flt