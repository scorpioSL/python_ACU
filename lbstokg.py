weight = input("Enter your weight ")
delimiter = input("lbs or kg? ")
if(delimiter == "lbs"):
    print("Your weight in kg is " + str(float(weight) * 0.45))
elif(delimiter == "kg"):
    print("Your weight in lbs is " + str(float(weight) / 0.45))