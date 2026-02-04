# Hardcoded values for the season and plant type

season = input("Enter the season (e.g., summer, winter): ") 
plant_type = input("Enter the plant type (e.g., flower, vegetable): ") #added input for plant type 

# Variable to hold gardening advice
advice = ""

if not season or not plant_type:
    advice = "Please provide both season and plant type."
else: 
    print ("Generating gardening advice...\n")

# Determine advice based on the season
# This block checks the season and adds specific advice for summer and winter. If the season is not recognized, it provides a default message.
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
    suggested_plant = "sunflower"  # Suggested plant for summer
    advice += f"Consider planting {suggested_plant}s for a vibrant garden.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
    suggested_plant = "pansy"  # Suggested plant for winter
    advice += f"Consider planting {suggested_plant}s for winter color.\n"
else:
    advice += "No advice for this season.\n"

# Determine advice based on the plant type
# This block checks the plant type and adds specific advice for flowers and vegetables. If the plant type is not recognized, it provides a default message.
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
    suggested_plant = "rose"  # Suggested flower
    advice += f" Consider planting {suggested_plant}s for a beautiful garden."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
    suggested_plant = "tomato"  # Suggested vegetable
    advice += f" Consider planting {suggested_plant}s for a tasty harvest."
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)


