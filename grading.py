# create a program that checks a student performance
marks=int(input("enter marks"))
if 100>= marks >= 80:
    print("you have an A")
elif 79>= marks >= 70:
    print("you have an B")
elif marks<=59 and marks>=40:
    print("you have an C")
elif marks>=39 and marks >=0:
    print("you have Failed")
#  create a program tht is going to calculate bmi
# BMI Calculator Program

def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return None  # Return None if height is zero to avoid division error


def bmi_category(bmi):
    if bmi is None:
        return "Invalid height entered."
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


# Taking user input with error checking
try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Check if BMI is None (invalid height input)
    if bmi is not None:
        print(f"\nYour BMI is: {bmi}")
        print(f"Based on your BMI, you are categorized as: {bmi_category(bmi)}")
    else:
        print("Height cannot be zero.")
except ValueError:
    print("Please enter valid numbers for weight and height.")














