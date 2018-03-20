# Binary search 
# bsearch.py
def search (items , target):
  low = 0
  high = len(items) - 1
  while low <= high: # There is still a range to search II 2
    mid = (low + high)//2 # position of middle item
    item = items[mid]
    if target == item :# Found it! Return the index 
      return mid
    elif target < item:# x is in lower half of range
      high = mid - 1# move top marker down
    else: # x is in upper half
      low = mid + 1# move bottom marker up
  return -1 # no range left to search
            # x is not there

  
