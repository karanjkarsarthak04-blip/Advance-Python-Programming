import logging

# Step 1: Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")

# Step 2: Define a function with debug logging
def divide(a, b):
    logging.debug("divide() called with a=%s, b=%s", a, b)
    result = a / b
    logging.debug("Result of division: %s", result)
    return result

# Step 3: Take input and handle exceptions
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    logging.info("User entered %s and %s", x, y)

    answer = divide(x, y)
    print("Result:", answer)
    logging.info("Division completed successfully")

except ValueError:
    print("Please enter valid integers.")
    logging.error("Invalid input entered", exc_info=True)

except ZeroDivisionError:
    print("Cannot divide by zero.")
    logging.exception("Division by zero attempted")

finally:
    logging.info("Program ended")
    print("Check app.log for the log records.")