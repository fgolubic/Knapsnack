'''
Created on Dec 4, 2018

@author: fgolubic
'''

#(category, price, satisfaction)
items = [(0,10,6), (1,12,6), (1, 11, 4), (1,8,2), (2, 20, 8), (2, 24, 10), (3, 3, 15)]
        
table = [[0 for i in range(50)] for i in range(7)]
keepTable = [[0 for i in range(50)] for i in range(7)]

itemNumber = 0
tableRow = 0
numberOfItemsProcessedByCategory = [0,0,0,0]
currentMax = 0
offsetedCurrentMax = 0
numberOfCategories = 4

for i in range(numberOfCategories):
    
    for j in items:
        
        if i == 0:
            #only if first considered category apply slightly different algorithm 
            if j[0] == i:
                
                itemNumber +=1
                numberOfItemsProcessedByCategory[i] += 1
                
                for k in range(36):
                    
                    for l in range(numberOfItemsProcessedByCategory[0]):
                        if currentMax < table[tableRow-l-1][k]:
                            currentMax = table[tableRow-l-1][k]
                            
                    
                    if k >= j[1]:
                        if currentMax > j[2]:
                            table[tableRow][k] = currentMax
                        else:
                            table[tableRow][k] = j[2]
                            keepTable[tableRow][k] = 1
                        
                    else:
                        table[tableRow][k] = currentMax
                    
                    currentMax =0
                tableRow+=1
                    
                    
        else:
            #for every other non-first category
            if j[0] == i:
                
                itemNumber+=1
                numberOfItemsProcessedByCategory[i] += 1
                
                for k in range(36):
                    
                    #check every item in last category and find max value
                    for l in range(numberOfItemsProcessedByCategory[i-1]):
                        elementForCheck = tableRow - (l+1+(numberOfItemsProcessedByCategory[i]-1))
                        
                        if currentMax < table[elementForCheck][k]:
                            currentMax = table[elementForCheck][k]
                    
                    #current weight less then current item weight write current max  
                    if j[1] > k:
                            table[tableRow][k] = currentMax
                            
                    else:
                        #check every item in last category and find max value offsetted 
                        #for weight of current item
                        for l in range(numberOfItemsProcessedByCategory[i-1]):
                            elementForCheck =  tableRow - (l+1+(numberOfItemsProcessedByCategory[i]-1))
                            
                            if offsetedCurrentMax < table[elementForCheck][k-j[1]]: 
                                offsetedCurrentMax = table[elementForCheck][k-j[1]]
                                
                        #value of item and value of remaining of weight    
                        element = j[2] + offsetedCurrentMax
                            
                        if currentMax > element:
                            table[tableRow][k] = currentMax
                                
                        else:
                            table[tableRow][k] = element
                            keepTable[tableRow][k] = 1
                
                    #reset temporary variables
                    currentMax = 0
                    offsetedCurrentMax = 0
                    
                tableRow += 1
   
   
   


print("Input data : (category, price, satisfaction):")

for i in items: 
    print(i) 
    
    
print
print

print("FILLED TABLE:\n")

for row in table:
    print(["{:2}".format(e) for e in row ])
   

print
print

print("FILLED KEEP TABLE:\n")

for row in keepTable:
    print(["{:2}".format(e) for e in row ])


print
print

itemIndex = tableRow - 1
price = 35
n = numberOfCategories

print("Optimal items: \n")
while(itemIndex >= 0 and price > 0):
    
    if keepTable[itemIndex][price] == 1:
        
        print(items[itemIndex])
        price-=items[itemIndex][1]
        itemIndex-=numberOfItemsProcessedByCategory[n-1]
        
        n-=1
        
    else:
        itemIndex-=1
