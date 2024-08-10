user_input = input("Enter numbers separated by space: ").split()
for n in range(0,len(user_input)):
    user_input[n]=int(user_input[n])
print("Highest number:", max(user_input))
print("Lowest number:", min(user_input))
