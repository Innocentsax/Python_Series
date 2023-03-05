"""CAR GAME"""
import time
started = False
while True:
  type = input("> ").lower()

  if type == "help":
    start= "Start - start the car"
    print(start)
    time.sleep(1)
    stop = "Stop - to stop the car"
    print(stop)
    time.sleep(2)
    quit = "Quit- to exit"
    print(quit)
    time.sleep(2)
  elif type == "start":
    if started:
      print("Car is already started!")
    else:
      started = True
      print("Car start ... Ready to go")
  elif type == "stop":
    if not started:
      print("Car is already stopped")
    else:
      started = False
      print("Car stop")
  elif type == "quit":
      break
  else:
    print("I don't understand that...")
