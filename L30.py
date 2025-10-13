# Program demonstrating string operations in Python

# Step 1: Create two strings
first_name = "Mizanur"
last_name = "Rahman"

# Step 2: Concatenate strings
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# Step 3: Find the length of the string
print("Length of Full Name:", len(full_name))

# Step 4: Convert to uppercase and lowercase
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())

# Step 5: String slicing
print("First 5 characters:", full_name[:5])
print("Last 3 characters:", full_name[-3:])

# Step 6: Check if a word exists in the string
if "Rahman" in full_name:
    print("'Rahman' is present in the name.")
else:
    print("'Rahman' is not present in the name.")

# Step 7: Replace a word
new_name = full_name.replace("Rahman", "Islam")
print("After replacement:", new_name)

# Step 8: Split the string into parts
name_parts = full_name.split(" ")
print("Split into parts:", name_parts)
