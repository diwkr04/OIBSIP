def calc_bmi(mass, height):
    bmi = mass / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    mass = float(input("Enter your mass in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calc_bmi(mass, height)
    category = classify_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

main()