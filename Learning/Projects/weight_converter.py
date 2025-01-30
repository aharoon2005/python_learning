weight = float(input("Enter a weight"))
weight_type = input("in lbs or kg?")
lbs = " lbs"
kg = " kg"

if weight_type == "kg":
    print(str(weight * 2.20462) + lbs)
elif weight_type == "lbs":
    print(str(weight * 0.453592) + kg)
else:
    print(f"Weight type is invalid")