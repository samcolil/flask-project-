# Step 1: Import necessary modules and create a Flask app instance.

from flask import Flask, request, render_template

app = Flask(__name__, template_folder="template")

# Step 2: Define a route for the home page ("/") that serves the calculation form.

@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        # Step 3: Handle form submissions.
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        # Step 4: Calculate the result based on the selected operation.
        if operation == 'addition':
            result = num1 + num2
            operation_name = 'Addition'
        elif operation == 'subtraction':
            result = num1 - num2
            operation_name = 'Subtraction'
        elif operation == 'multiplication':
            result = num1 * num2
            operation_name = 'Multiplication'
        elif operation == 'division':
            if num2 == 0:
                result = 'Cannot divide by zero'
                operation_name = 'Division'
            else:
                result = num1 / num2
                operation_name = 'Division'
        else:
            result = 'Invalid operation'
            operation_name = 'Invalid Operation'

        # Step 5: Render the template with the result.
        return render_template('index.html', result=result, operation_name=operation_name)

    # Step 6: Serve the calculation form initially.
    return render_template('index.html')

# Step 7: Run the Flask application.
if __name__ == '__main__':
    app.run(debug=True)
