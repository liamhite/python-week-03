print("click on terminal!!!")

try:
  speed = int(input("enter speed: "))
  speedLimit = int(input("enter speed limit: "))

  diff = speed - speedLimit 
  print("diff = " + str(diff) + "mph")

  if speed <= speedLimit or diff < 5:
    print("no fine")

  if diff >= 5 and diff < 10:
    print("fine $10")

  if diff >= 10 and diff < 15:
    print("fine $20")

  if diff >= 15 and diff < 20:
    print("fine $30")

  if diff >= 20 and diff < 25: 
    print("fine $40")

  if diff >= 25 and diff < 30:
    print("fine $50")

  if diff >= 30 and diff < 35:
    print("fine $50")

  if diff >= 35 and diff < 40:
    print("fine $60")

  if diff >= 40 and diff < 45:
    print("fine $70")

  if diff >= 45 and diff < 50:
    print("fine $80")

  if diff >= 50 and diff < 55: 
    print("fine $90")

  if diff >= 55 and diff < 60:
    print("fine $100")

  if diff >= 60 and diff < 65:
    print("fine $110")
    
  if diff >= 65:
    print("wicked fast")
    print("fine $150")

except ValueError:
  print("Please enter a valid integer.")

