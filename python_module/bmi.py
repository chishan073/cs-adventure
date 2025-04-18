def bmi(height, weight):
    """
    Calculate the Body Mass Index (BMI) using the formula:
    BMI = weight (kg) / (height (m))^2

    Parameters:
    height (float): Height in centimeters. Must be greater than 0.
    weight (float): Weight in kilograms. Must be greater than 0.
    """
    # Check if height is greater than zero
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    # Convert height from cm to m
    height_m = height / 100
    # Calculate BMI
    bmi_value = weight / (height_m ** 2)
    return bmi_value

def bmi_category(bmi_value):
    """
    Determine the BMI category based on the BMI value.
    """
    if bmi_value < 18.5:
        return "過輕"
    elif 18.5 <= bmi_value < 24:
        return "正常"
    elif 24 <= bmi_value < 27:
        return "過重"
    else:
        return "肥胖"

# Example usage
if __name__ == "__main__":
    # Input height and weight
    height = float(input("請輸入身高 (cm): "))
    weight = float(input("請輸入體重 (kg): "))

    # Calculate BMI
    bmi_value = bmi(height, weight)
    print(f"您的 BMI 值為: {bmi_value:.2f}")

    # Determine BMI category
    category = bmi_category(bmi_value)
    print(f"您的 BMI 類別為: {category}")