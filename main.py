x = 0
while x <= 20:
  if x/3 - int(x/3) == 0 and x > 0:
    if x/4 - int(x/4) == 0:
      print("foo buzz", x)
    else:
      print("buzz", x)
  elif x/4 - int(x/4) == 0 and x > 0:
      print("foo", x)
  elif isinstance(x, int) and x > 0:
    print(x)
  else:
    print("ready, set, go")
  x += 1
