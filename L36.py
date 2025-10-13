import calendar

# Get all month names
months = list(calendar.month_name)  # Returns a list from index 1 to 12 (index 0 is empty)

# Display months
for month in months[1:]:  # Skip the first empty element
    print(month)
