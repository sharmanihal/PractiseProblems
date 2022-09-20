from heapq import heapify, heappop, heappush


list=[2,3,1,4,5,34,6,89,99]
heap=[]
#if we want min heap 
for i in list:
    heappush(heap,i)

for i in range(len(heap)):
    print(heappop(heap))


#if we want max heap, we have multipy -1 so that max element becomes min and get to the top
maxHeap=[]
for i in list:
    heappush(maxHeap,i*-1)

for i in range(len(maxHeap)):
    print(-1*heappop(maxHeap))

#if we want to push pair in min heap with heap sorted on key( we can use sets)
minH = []
set=((5, 'write code'),(7, 'release product'),(1, 'write spec'),(3, 'create tests'))
for i in set:
    heappush(minH,i)
for i in range(len(minH)):
    print(heappop(minH))

#if we want to push pair in max heap with heap sorted on key(multipy key with -1 to make max key as min key)
print("")
maxH = []
set1=((5, 'write code'),(7, 'release product'),(1, 'write spec'),(3, 'create tests'))
for (key,val) in set1:
    heappush(maxH,(-1*key,val))
for i in range(len(maxH)):
    element= heappop(maxH)
    print((-1*element[0],element[1]))

#heapify the list
print("")
list1=[2,3,1,4,5,34,6,89,99]
heapify(list1)
print(list1)