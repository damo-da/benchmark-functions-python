# Place the functions that you want to compare on this file.
# These sort{0...4} are simple insertion sorting algorithms, to allow users to test. 
# You can remove them at your ocnvenience.

def sort0(arrayToSort):
    sortedArray = [];
    sortedArray.append(arrayToSort[0]);
    for j in range(1, len(arrayToSort)):
        key = arrayToSort[j];   
        sortedArray.append(key);  
        i = j -1;

        while i >= 0 and sortedArray[i] > key:
            temp = sortedArray[i +1];         
            sortedArray[i +1] = sortedArray[i];
            sortedArray[i] = temp;
            i = i-1;
    return sortedArray

def sort4(arrayToSort):
    sortedArray = [];
    sortedArray.append(arrayToSort[0]);  

    for index, key in enumerate(arrayToSort[1:]):
        sortedArray.append(key);  
        i = index; 

        while i >= 0 and sortedArray[i] > key:
            temp = sortedArray[i +1];         
            sortedArray[i +1] = sortedArray[i];
            sortedArray[i] = temp;
            i = i-1;
        
    return sortedArray

def sort3(arrayToSort):
    sortedArray = [arrayToSort[0]];

    for index, key in enumerate(arrayToSort[1:]):
        sortedArray.append(key);  
        i = index; 

        while i >= 0 and sortedArray[i] > key:
            temp = sortedArray[i +1];         
            sortedArray[i +1] = sortedArray[i];
            sortedArray[i] = temp;
            i = i-1;
        
    return sortedArray


def sort2(arrayToSort):
    sortedArray = [arrayToSort[0]];

    for index, key in enumerate(arrayToSort[1:]):
        sortedArray.append(key);  
        i = index; 

        while i >= 0 and sortedArray[i] > key:
            sortedArray[i+1],sortedArray[i] = sortedArray[i],sortedArray[i+1]
            i = i-1;
        
    return sortedArray

def sort1(arrayToSort):
    sortedArray = [arrayToSort[0]];

    for i, key in enumerate(arrayToSort[1:]):
        sortedArray.append(key);  

        while i >= 0 and sortedArray[i] > key:
            sortedArray[i+1],sortedArray[i] = sortedArray[i],sortedArray[i+1]
            i = i-1;
        
    return sortedArray

def sort5(arrayToSort):
    sortedArray = [arrayToSort[0]];

    for i, key in enumerate(arrayToSort[1:]):
        sortedArray.append(key);  

        while i >= 0 and sortedArray[i] > key:
            sortedArray[i+1],sortedArray[i] = sortedArray[i],sortedArray[i+1]
            i = i-1;
        
    return sortedArray
