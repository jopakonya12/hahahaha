#create a list of numbers from 1 to 50
numbers = list(range(1, 51))

#filter out the even numbers
even_numbers = [number for number in numbers if number % 2 == 0]

#print the even numbers
print(even_numbers)

