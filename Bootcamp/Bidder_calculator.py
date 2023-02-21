
print("BIDDER CALCULATOR")
import os, time
while True:
  
  bids = {} # an empty dictionary ==> name(key): $100(value)

  name = input("What is your name: ")
  #time.sleep(1)
  price = int(input("What's your bid:$ "))
  bids[name] = price
  #time.sleep(1)
  should_continue = input("Are there any other bidders? Type 'Yes' or 'No': ")
  if should_continue == 'No':
    break
  else:
    time.sleep(1)
    os.system("clear")
    continue
  
highest_bids = 0
for bidder in bids:
  if bids[bidder] > highest_bids:
    highest_bids = bids[bidder]
    winner_name = bidder

print(f"The winner {winner_name} with a bid of ${highest_bids}")
