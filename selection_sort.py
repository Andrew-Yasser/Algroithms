#how this function finds the smallest element of the array.
def findSmallest(arr): #function with a parameter to hold an array
  smallest = arr[0]  #stores the smallest value
  smallest_index = 0 
  for i in range(1, len(arr)): 
    if arr[i] < smallest: #if the value in the array at the index of i is smaller than the value at the index of 0
      smallest_index = i #stores the index of the smallest number  (position of i)
      smallest = arr[i] #the smallest number is now the number at the index of i     
  return smallest_index #return the index position of the smallest number

def selectionSort(arr): #function to sort the array
  newArr = [] 
  for i in range(len(arr)): #loop through passed array
      smallest = findSmallest(arr) #Finds the smallest element in the array, and adds it to the new array
      newArr.append(arr.pop(smallest)) #remove the smallest number from the passed array and add it to the new one. Repeat until passed array is empty
  return newArr #return the new array

print(selectionSort([5, 7, 6, 2, 10]))
