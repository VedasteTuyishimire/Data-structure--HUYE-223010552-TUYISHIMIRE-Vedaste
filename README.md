1.

temperatures = []

for day in range(1, 8):
    temp = float(input(f"Enter temperature for day {day}: "))
    temperatures.append(temp)

print("Temperatures for the week:")
for day, temp in enumerate(temperatures, 1):
    print(f"Day {day}: {temp:.2f}")

2. 

sales = []

for day in range(1, 8):
    sale = float(input(f"Enter sales for day {day}: "))
    sales.append(sale)

average_sales = sum(sales) / len(sales)
print("Average daily sales:", average_sales)

3.

stock_prices = []

for day in range(1, 8):
    price = float(input(f"Enter stock price for day {day}: "))
    stock_prices.append(price)

max_price = max(stock_prices)
min_price = min(stock_prices)

print("Maximum price:", max_price)
print("Minimum price:", min_price)

4.

marks = []

for student in range(1, 8):
    mark = int(input(f"Enter mark for student {student}: "))
    marks.append(mark)

marks.reverse()
print("Reversed marks:", marks)

5.

import random

random_numbers = [random.randint(1, 100) for _ in range(10)]

even_count = 0
odd_count = 0

for number in random_numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

7.

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

# Create a 3x3 tic-tac-toe board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Fill the board with moves (replace ' ' with 'X' or 'O')
# ...

winner = check_winner(board)
if winner:
    print(f"{winner} has won!")
else:
    print("It's a tie!")

7. 
products = ["Product A", "Product B", "Product C"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

sales = [[0 for _ in range(len(days))] for _ in range(len(products))]

# Fill the sales data
# ...

for i, product in enumerate(products):
    print(f"{product}:")
    for j, day in enumerate(days):
        print(f"\t{day}: {sales[i][j]}")

8. 

import numpy as np

image = np.random.randint(0, 256, (100, 100, 3))  # Example 100x100 RGB image

inverted_image = 255 - image

# Display the images (using a library like OpenCV or Matplotlib)

9.

students = ["Student 1", "Student 2", "Student 3"]
subjects = ["Math", "Science", "English"]

marks = [[0 for _ in range(len(subjects))] for _ in range(len(students))]

# Fill the marks data
# ...

for i, student in enumerate(students):
    total_marks = sum(marks[i])
    print(f"{student}: Total marks = {total_marks}")

10.

cities = ["City A", "City B", "City C", "City D"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

temperatures = [[[0 for _ in range(len(days))] for _ in range(len(cities))] for _ in range(len(cities))]

# Fill the temperature data
# ...

for i, city in enumerate(cities):
    total_temp = 0
    for j, day in enumerate(days):
        total_temp += temperatures[i][j]
    average_temp = total_temp / len(days)
    print(f"{city}: Average temperature = {average_temp:.2f}")

