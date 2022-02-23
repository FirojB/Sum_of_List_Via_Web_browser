# Importing the library for flask server communication
from flask import Flask

# Execution for the main program
app = Flask(__name__)


# Call the function when endpoint encounter "/total" in address bar
@app.route("/total")
def list_sum():

    # List received from background services
    numbers_to_add = list(range(10000001))

    # Initialising the value to zero
    total = 0

    # Iteration for elements in the list
    for item in numbers_to_add:

      # Adding the elements of the list
      total = total + item

    # Dictionary creation
    dict_total = {
        "Total ": total
    }

    # Returning the total in the form of Dictionary
    return dict_total

# Call the function when endpoint encounter "/number" in address bar
@app.route("/<int:num>")

# Pass the number to the function as
def list_add(num):

    # number received from background services via address bar
    numbers_to_add = list(range(num))

    # Initialising the value to zero
    total = 0

    # Iteration for elements in the list
    for item in numbers_to_add:

      # Adding the elements of the list
      total = total + item

    # Dictionary creation
    dict_total = {
        "Total ": total
    }

    # Returning the total in the form of Dictionary
    return dict_total
