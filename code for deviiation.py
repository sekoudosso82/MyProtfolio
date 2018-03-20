import math
def main() :
  self = [1,2,3,4,5]
  summ = 0
  
  for i in range (len(self)):
    summ = summ + self[i] 
  average = summ/len(self)

  summ = 0.0
  xStr = average
  for i in range (len(self)):
    summ1 = (xStr - self[i])**2
    summ += summ1
  deviation = math.sqrt(summ/ (len(self) -1))
  
  print( " this is the summ of this list self; ",self)
  print( " this is the summ of this list self; ",summ)
  print( " this is the average of this list self; ",average)
  print( " this is the deviation of this list self; ",deviation)

        
  
main()

  
