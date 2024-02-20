def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average

def main():
    """Main function."""
    numbers = [10, 20, 30, 40, 50]
    average = calculate_average(numbers)
    print(f"The average of the numbers is: {average}")

if __name__ == "__main__":
    main()
