# given coordinates of vector, output the coordinates of where the vector lands
def intersection(iHat, jHat, result):
  if len(result) != len(iHat) or len(result) != len(jHat):
    return "Not a square matrix"
  else:
    for i in range(len(iHat)):
      result[i] = result[i]*iHat[i]
      for j in range(len(jHat)):
        result[j] = result[j]*jHat[j]
    
  
