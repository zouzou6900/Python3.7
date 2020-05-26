pot=1
mise=1
misee=0
i=0
while pot <= 100000000:
    i+=mise
    if i <2:
        misee=mise *mise
        pot = pot * misee
        
    elif i ==2:
        mise1=2
        misee=pot *mise1
        pot = pot * misee
        
    elif i > 2:
         pot = pot * misee
    print("jour ",i)    
    print("je recois ",pot/100)

