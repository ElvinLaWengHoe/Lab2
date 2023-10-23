'''def calculate_bmi(height, weight,bmi):
    print("Height = " + height)
    print("Weight = " + weight)
    print("BMI = " + bmi)

    bmi = weight/(height ** 2)
    return bmi



weight = 57
height = 1.73
calculate_bmi(weight, height)'''


def calculate_bmi(weight_kg, height_m):
    # Check for invalid input
    if weight_kg <= 0 or height_m <= 0:
        return "Invalid input. Weight and height must be positive numbers."

    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)

    if bmi < 18.5:
        print("You are Under Weight")
    elif 18.5 <= bmi <= 25.0 :
        print("You are Normal Weight")
    else : print("You are Over Weight")
    return bmi




# Example usage:
weight = 60  # weight in kilograms
height = 1.75  # height in meters
bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")

