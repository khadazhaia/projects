import math

# Welcome message, take in the name of the participant and greet them
print('''Welcome to the CLI Health Monitoring App\n
You will be able to obtain the maximum, minimum, average and standard deviation of your heart rate\n''')

name = input("To start please enter your name: ").capitalize().strip()

print(f"\nHello {name}, now collect 8 hours worth of heart rate data\n")

# Using a for-loop, collect 8 hours worth of heart rate data using the input() function. Ensure that each value that's added to the list is strictly an integer 
heart_rates = []
hour = 1

for h in range(8):
  while True:
    hour_input = input(f"Hour {hour}: ")
    print()
    if hour_input.isdigit():
      h = int(hour_input)
      if h >= 40 and h <= 190:
        heart_rates.append(h)
        hour += 1
        break
      else:
        print("Try Again. Please enter a number between 40 and 190\n")
    else:
        print("Try Again. Please enter only whole numbers\n")

# Once you've completed this data collection, calculate the maximum, minimum, average, and the standard deviation of the heart rate.
# calculate the maximum 
max_rate = max(heart_rates)
print(f"{name}, your maximum heart rate is {max_rate}\n")

# calculate the minimum 
min_rate = min(heart_rates)
print(f"{name}, your minimum heart rate is {min_rate}\n")

# calculate the average
average_rate = sum(heart_rates) // len(heart_rates)
print(f"{name}, your average heart rate is {average_rate}\n")

# To calculate the standard deviation of a set of data, follow these steps:

# Subtract the average from each data point and then square it
square_diff = []

for s in heart_rates:
    sd = (s - average_rate) ** 2
    square_diff.append(sd)    
      
# Calculate the variance: Find the average of the squared differences
variance = sum(square_diff) / len(square_diff)
  
# Calculate the standard deviation: Find the square root of the variance 
standard_dev = math.sqrt(variance)
print(f"{name}, your standard deviation heart rate is {standard_dev:.02f}\n")

# The standard deviation is a measure of how spread out the values in a dataset are. A high standard deviation means the values are generally far from the mean, while a low standard deviation means the values are close to the mean. 