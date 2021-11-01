#Transport kosten berekenen Tim Koole

weight = 41.5

# "Ground Shipping"

if weight <= 2:
  ground_shipping_cost = weight * 1.50 + 20
elif weight <= 6:
  ground_shipping_cost = weight * 3.00 + 20
elif weight <= 10:
  ground_shipping_cost = weight * 4.00 + 20
else:
  ground_shipping_cost = weight * 4.75 + 20  

print("Uw kosten voor Ground Shipping zijn:")
print(ground_shipping_cost)  

# "Premium Ground Shipping"

premium_ground_shipping_cost = 125

print("Uw kosten voor Premium Ground Shipping zijn:")
print(premium_ground_shipping_cost)

# "Drone Shipping"

if weight <= 2:
  drone_shipping_cost = weight * 4.50
elif weight <= 6:
  drone_shipping_cost = weight * 9.00
elif weight <= 10:
  drone_shipping_cost = weight * 12.00
else:
  drone_shipping_cost = weight * 14.25

print("Uw kosten voor Drone Shipping zijn:")

print(drone_shipping_cost)
