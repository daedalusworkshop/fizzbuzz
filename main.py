# The FizzBuzz problem is a classic test given in coding interviews. The task is simple: Print integers 1 to N, but print “Fizz” if an integer is divisible by 3, “Buzz” if an integer is divisible by 5, and “FizzBuzz” if an integer is divisible by both 3 and 5.

x = 0
n = 20
while x <= n:
  if x/3 - int(x/3) == 0 and x > 0:
    if x/4 - int(x/4) == 0:
      print("Fizz buzz", x)
    else:
      print("Fizz", x)
  elif x/5 - int(x/5) == 0 and x > 0:
      print("Buzz", x)
  elif isinstance(x, int) and x > 0:
    print(x)
  else:
    print("ready, set, go")
  x += 1
