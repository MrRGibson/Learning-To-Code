tickets = [""]
filmName = input("Enter film name:")
ticketNumber = int(input("Enter ticket number:"))
totalCost = 0.00

while ticketNumber <1 or ticketNumber >5:
  print("Invalid ticket number")
  ticketNumber = int(input("Enter ticket number:"))

for i in range(ticketNumber):
  ticketType = str(input("Enter ticket type:"))
  if ticketType == "A":
      totalCost = totalCost + 8.50
      tickets.append("Adult")
  elif ticketType == "C":
      totalCost = totalCost + 4.90
      tickets.append("Child")
  elif ticketType == "S":
      totalCost = totalCost + 5.50
      tickets.append("Student")
  elif ticketType == "O":
      totalCost = totalCost + 4.00
      tickets.append("OAP")
  else:
      print("Please enter a valid ticket type")
      ticketType = str(input("Enter ticket type:"))

print("The tickets purchased were:")
for x in tickets:
  print(x)

print("The total cost of tickets purchased for " + filmName + "was £",totalCost)