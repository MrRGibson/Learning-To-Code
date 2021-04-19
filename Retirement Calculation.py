import datetime

currentYear = datetime.datetime.now()
currentYear = int(currentYear.strftime("%Y"))

currentAge = input("What is your current age?")
retirementAge = input("At what age would you like to retire?")

retirement = int(retirementAge) - int(currentAge)
retirementYear = currentYear + retirement

print("You have {} years left until you can retire.".format(retirement))
print("It's {}, so you can retire in {}".format(currentYear, retirementYear))
