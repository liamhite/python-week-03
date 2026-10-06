try:
  speedLimit = int(input("enter speed limit: "))
  speed = int(input("enter speed: "))
  
  diff = speed - speedLimit 
  print("diff = " + str(diff) + "mph")

  if speed <= speedLimit or diff < 5:
    print("no fine")

  elif diff >= 5 and diff < 15:
    print("fine $10")

  elif diff >= 15 and diff < 25:
    print("fine $20")

  elif diff >= 25 and diff < 40:
    print("fine $40")

  else:
   print("wicked fast") 
   print("fine $60")

except ValueError:
  print("Please enter a valid integer.")