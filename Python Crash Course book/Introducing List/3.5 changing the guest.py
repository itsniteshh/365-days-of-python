guest = ["tesla", "king ashoka", "Chandragupta", "Alexander"]

print(f"You are invited for the dinner, {guest[0]}")
print(f"You are invited for the dinner, {guest[1]}")
print(f"You are invited for the dinner, {guest[2]}")
print(f"You are invited for the diner, {guest[-1]}")

print(f"Sorry guys, but it seems {guest.pop(2)} won't be able to make it")
print(f"{guest.append("first human")}, you are invited to the dinner")

print(guest)