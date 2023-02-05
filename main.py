height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

h=height;
w=weight;

bmi =float("{:.2f}".format(w/(h*h)))

if bmi<18.5:
    print("Your BMI is " + str(bmi) +" and you are underweight.")
elif bmi>=18.5 and bmi<25.0:
    print("Your BMI is " + str(bmi) +" and you have a normal weight.")

elif bmi>=25 and bmi<30:
    print("Your BMI is " + str(bmi) +" and you are slightly overweight.")


elif bmi>=30 and bmi<35:
    print("Your BMI is " + str(bmi) +" and you are obese.")


elif bmi>=35:
    print("Your BMI is " + str(bmi) +" and you are clinincally obese.")