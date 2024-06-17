def calculate_bmi(weight, height):
    """Calculate BMI and classify into categories."""
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return bmi, category

def main():
    print("Welcome to the BMI Calculator!")

    # Get user input for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI and get category
    bmi, category = calculate_bmi(weight, height)

    # Display results
    print(f"\nBMI: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
