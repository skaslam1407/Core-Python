str = "hello world"
l = list(str)
print(l)
print(type(l))
  

def displayCount(l,m=0):
    count = 0
    for i in l:
        count += 1
    return count + m

l = ['h', 'e', 'l', 'l', 'o']     

rv = displayCount(l,m=10)

print("The count of elements in the list is:", rv)
