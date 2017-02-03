+Author: Sam
 +Credit: none
  Assignment:
  
  Write and submit a Python program that computes an approximate value of π by calculating the following sum:
 @@ -21,3 +21,9 @@
  Note: remember that the printed value of pi will be an estimate!
  
  """
import math
n = int(input("I will estimate pi. How many terms should I use? "))
decimals = int(input("How many decimal places should I use in the result? "))
pi = 4*sum([((-1.0)**k)/((2*k+1)) for k in range(0,n)])
print("The approximate value of pi is {0}".format(round(pi, decimals)))

