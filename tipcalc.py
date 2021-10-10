# Static variables for limit on individual diners for complex calculation and tax percentage
propLimit = 12
taxPct = 0.10

#Function to take in the number of diners splitting the bill and call the next step of the program
def dinersFunct ():
    
    try:
        diners = int(input('How many diners are splitting the tip: '))
    except:
        print("Please input a number")
        dinersFunct()
        print()
    return diners

#Function to display choice of how to split the bill (evenly or porportionally) then move on to next step
def evenPropFunct ():
    evenOrProp = input('Are we splitting the bill evenly or proportionally? Enter 1 for evenly, 2 for proportionally: ')
    print()
    if str(evenOrProp) == "1":
        return evenOrProp
    elif str(evenOrProp) == "2":
        return evenOrProp
    else:
        print('Please input a number')
        evenPropFunct()

#Function to calculate and display bill if evenly split
def simpleBill(diners):

   try: 
        billTot = float(input("What is the bill total: "))
   except:
       print('Please input a number')
       simpleBill(diners)

   try:
        tipPct = float(input("What is the desired tip percentage: "))
   except:
       print('Please input a number')
       simpleBill(diners)

   dinerTax = round(((billTot * taxPct) / diners),2)
   dinerTab = round(float(billTot/diners),2) 
   dinerTip = round(round(billTot * (tipPct/100),2)/diners,2)
   dinerTotal = round(dinerTab + dinerTax + dinerTip,2)
   print()

   print('DINERS TABS')
   print('Tab: $' + str(dinerTab))
   print('Tax: $' + str(dinerTax))
   print('Total with Tax: $' + str(dinerTab + dinerTax))
   print('Tip: $' + str(dinerTip))
   print('Grand Total: $' + str(dinerTotal))
   print()

   print('TOTAL')
   print('Tab: $' + str(round(billTot,2)))
   print('Tax: $' + str(round(billTot * taxPct,2)))
   print('Total with Tax: $' + str(round((round(billTot,2) * round(taxPct,2)),2) + round(billTot,2)))
   print('Tip: $' + str(round((billTot * (tipPct/100)),2)))
   print('Grand Total: $' + str((round((billTot * (tipPct/100)),2) + round((round(billTot,2) * round(taxPct,2)),2) + round(billTot,2))))


#Function to split bill and calculate and display in more robust manner, bill spit porportionally and individual tip percentages
def complexBill(dinersList):
        dinersList = proportionalDict(diners)
        totalTab = 0
        totalTax = 0
        totalTip = 0
        totalWithTip = 0

        for diner in dinersList:
              dinerName = diner['Name']
              dinerTab = round(float(diner['Tab']),2)
              dinerTip = round(float(diner['Tip'])/100,2)
              dinerTax = round(float(taxPct),2) * round(float(diner['Tab']),2)
              calcTip = round(float(dinerTab),2) * round(dinerTip,2)
              print('Receipt for ' + dinerName)
              print('Tab: $' + str(round(dinerTab,2)))
              print('Tax: $' + str(round(dinerTax,2)))
              print('Total with Tax: $' + str(round(round(dinerTab,2) + round(dinerTax,2),2)))
              print('Tip: $' + str(round(calcTip,2)))
              print('Total: $' + str(round((round(dinerTab,2) + round(dinerTax,2) + round(calcTip,2)),2)))
              print()
              totalTab += round(dinerTab,2)
              totalTax += round(dinerTax,2)
              totalTip += round(calcTip,2)
              totalWithTip += round((round(dinerTab,2) + round(dinerTax,2) + round(calcTip,2)),2)
        print('TOTAL')
        print('Tab $' + str(round(totalTab,2)))
        print('Tax $' + str(round(totalTax,2)))
        print('Tip $' + str(round(totalTip,2)))
        print('Grand Total $' + str(round(totalWithTip,2)))

#Function to store input number of diners in the party and capture their bill info for use in complex calculation
def proportionalDict(diners):
    dinersList = []
    i = 0
    while i < diners:
        dinerName = input("Diner Name: ")
        dinerTab = input("Diner Tab: ")
        dinerTip = input("Tip Percent: ")
        loopDict = {
                    "Name" : dinerName,
                    "Tab" : dinerTab,
                    "Tip" : dinerTip
                    }
        print()
        dinersList.append(loopDict)
        i += 1
    return dinersList


# Executes the calculation for either a simple or cimplex bill.
diners = dinersFunct()

if diners <= propLimit:
    #If diners in party less than limit for complex bill, display choice to split evenly or proportionally
    splitFlag = evenPropFunct()
    
    #If evenPropFunct returs choice to split proportionally not evenly execute complex bill functions
    if splitFlag == "2":
        complexBill(diners)
    #Else execute simple bill calculation 
    else:
        simpleBill(diners)
#Else statement for if diniers great than diner limit for complex bill calculation, executes simple bill function
else:
    simpleBill(diners)
