# Ask a user to enter a number
# Ask a user to enter a second number
# Calculate the total of the two numbers added together
# Print 'first number + second number = answer' 
# For example if someone enters 4 and 6 the output should read
# 4 + 6 = 10
First_num = input("Give me a number: ")
Second_num = input("Give me a second number: ")
answer = float(First_num) + float(Second_num)
print(First_num + '+' + Second_num + '=' + str(round(answer)))
