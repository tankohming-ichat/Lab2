def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    #Add code here to calculate BMI
    bmi = weight/(height*height)
    #Add code here to display calculate BMI
    if (bmi < 18.5):
        string="Under Weight"
    elif (bmi < 25.0):
        string="Normal Weight"
    else:
        string="Over Weight"
    print("BMI is %s, which is %s" %(bmi,string))

calculate_bmi(weight=57, height=1.73)