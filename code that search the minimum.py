def main() :
  self = [1,2,3,4,5,6]
  min= self[2]
  for i in range (len(self)):
    if self[i]<min:
      min = self[i]
    else:
      min = min
      
  print(" The minimum of this list is :", min)
main()
