

def bubbleSort(inp):
    listLength=len(inp)
    for i in range(listLength-1):
        for j in range(listLength-i-1):
            if inp[j]>inp[j+1]:
                inp[j],inp[j+1]=inp[j+1],inp[j]
    return inp

print(bubbleSort([4,3,5,1,-1]))