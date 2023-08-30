#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Define the route for the root URL
@app.route('/')
def index():
    # Return the main heading for the web app
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Define a route that accepts a string parameter and displays it
@app.route('/print/<string:text>')
def print_string(text):
    # Print the input text to the console
    print(text)
    # Return the text to be displayed in the browser
    return f'{text}'

# Define a route that accepts an integer and displays a count up to that number
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = ""
    # Loop through the range up to the given parameter
    for i in range(parameter):
        # Append each number to the numbers string with a newline
        numbers += f"{i}\n"
    # Return the string of numbers to be displayed in the browser
    return numbers

# Define a route that performs mathematical operations based on URL parameters
@app.route('/math/<int:parameter1>/<string:operation>/<int:parameter2>')
def math(parameter1, operation, parameter2):
    # Check the operation and perform the corresponding arithmetic
    if operation == '+':
        return f'{parameter1 + parameter2}'
    elif operation == '-':
        return f'{parameter1 - parameter2}'
    elif operation == '*':
        return f'{parameter1 * parameter2}'
    # Use 'div' for division to avoid conflicts with URL special characters
    elif operation == 'div':
        return f'{parameter1 / parameter2}'
    elif operation == '%':
        return f'{parameter1 % parameter2}'
    else:
        # Return an error message if the operation is not recognized
        return 'Invalid operation'

# Check if this script is being run as the main module
if __name__ == '__main__':
    # Start the Flask development server on port 5555 with debugging enabled
    app.run(port=5555, debug=True)
