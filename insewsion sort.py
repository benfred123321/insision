# Step 1:asign the second element as the key value
# Step 2:compare the key to the lements before it 
# Step 3:if the key is less than any one oth the elements before it
# Step 4:shift all the elements grater than the key to the right
# Step 5:make the key the next element from the current key position 
# Step 6:repeat steps 2-5 until you reach the end of the list

import time

lists=[6,2,9,7,0,5,3,1,4,8,10]
startime=time.time()
for i in range(1,len(lists)):
    key = lists[i]
    j=i-1
    while key < lists[j] and j >= 0:
        lists[j+1] = lists[j]
        j=j-1
    
    lists[j+1] = key    
    print(key)
    print(lists)
endtime=time.time()        
print(endtime-startime)
