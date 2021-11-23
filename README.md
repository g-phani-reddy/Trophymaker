# Trophymaker
Trophymaker, is an MVP developed using python and flask for the API backend, gives the estimated cost in trophy making based on customer choice. This applications gives the flexiblity to the cusotmer to choose the parameters such as the shape, size, materials and coatings to be used and returns the estimated cost. The estimated cost depends on the volume, cost of the materials and coatings.

# Code description:
Pre-defined shapes and coating materials along with respective cost and ids are stored in List of dictionaries. For instances, shapes are stored in shapeslist and coating materials are stored in coatlist.

The selected shape and coating material indexes will be posted to shapes(), it will fetch the cost of the parameters and then call the calculateshape() based on the shape selected, here shape in the function name refers to the customer selected shape.

Then the calculate function calculates the volume and gives the resultant cost. The estimated cost will be displayed to the user on the screen.


# How to use the application:
Firstly, user can able to view the pre-defined shapes and coating materials with the respective unique ids.

Then the user can select based on their requirement and proceed to the next step. Give the measurements as required and then click to get the estimtaed cost for the selected parameters.

If the ids are choosen out of the scope, then error will pop up to select the proper id.

# Files description:
Code is placed in https://github.com/g-phani-reddy/Trophymaker/blob/main/app.py

All the templates are placed in https://github.com/g-phani-reddy/Trophymaker/tree/main/templates



