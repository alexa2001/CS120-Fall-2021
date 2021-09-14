#arr is array of (val, key) pairs
import math
import time
import random


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr2[i])
            i += 1
        else:
            sortedArr.append(arr1[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(arr, univsize):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def base_b(num, b): #converts any number to base b
  string =""

  # if num == 0:
  #   return 0

  while num > 0:
    string = str(num % b) + string
    num //= b
  return string 

#return ith digit of a number, reading right to left, beginning at 0
def ith_digit(num, dig):
  return num[0] // 10**dig % 10 

#makes a list of item, key pairs where the item is a number and the key is the ith digit of that number
def ith_list(arr, dig):
  ithlist = []
  for i in range(len(arr)):
    # tpl = ( ith_digit(arr[i], dig), arr[i])
    tpl = ( arr[i][0], ith_digit(arr[i], dig))
    ithlist.append(tpl)
  return ithlist 


#finds the number of digits in the biggest key of a list of (key, item) pairs
def length_of_max(arr):
  maxnum = 0 
  for i in range(len(arr)):
    if arr[i][0] > maxnum:
      maxnum = arr[i][0]
  count = 0
  while maxnum > 0:
    maxnum //= 10
    count += 1
  return count

def base_ten(num, b):
  ans = 0
  i = 0
  while num > 0:
    dig = (num % 10)*(b**i) #ai*b^i
    ans += dig
    num //= 10
    i+=1
  return ans

def radix_sort(arr, n, univsize, b):
    #makes a new list with the same item and new base b keys
    blist = []
    for key, item in arr: 
        t = ((int (base_b(key, b)), item))
        blist.append(t)

    #the list of keys
    # lst = [i[0] for i in blist] 

    #will put the keys in order 
    print("length_of_max(blist): ", length_of_max(blist))
    for i in range(length_of_max(blist)):
        lst = ith_list(blist, i)
        # print("lst: ", lst)
        sorted_lst = countSort(lst, univsize) #sorts by ith digit
        # print("sorted_lst: ", sorted_lst)

    #order the blist according to sorted lst
    ans=[]
    print("sorted_lst", sorted_lst)
    print("blist", blist)
    for j in range(n):
        for i in range(n):
            # print("sorted_lst[j][0], blist[i][1]: ", sorted_lst[j][0], blist[i][1])
            print("j, i: ", j, i)
            if sorted_lst[j][0] == blist[i][0]:
                ans.append(blist[i])
                blist.remove(blist[i])
                n -=1 
                break
    #return keys to base 10
    for i in range(len(ans)):
        ans[i] = ( base_ten((ans[i][0]), b), ans[i][1])
        print("ans[i]: ", ans[i])
    return ans

test_list1 = [(34, "a"), (600, "a"), (531, "a")]
test_list2 = [(335, "a"), (331, "b"), (331, "c")]
test_list3 = [(33, "a"), (35, "b"), (36, "a"), (30, "b")]
test_list4 = [(12, "a"), (11, "b"), (12, "c"), (15, "d")]
test_list5 = [(12, "a"), (9, "b"), (4, "c"), (2, "d")]
print( radix_sort(test_list2, 3, 1000000, 3) )
        

        

    
    
  
