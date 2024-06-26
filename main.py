
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
import subprocess

# Create a Flask app
app = Flask(__name__)

# Define the routes
@app.route('/')
def index():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/building-agents')
def building_agents():
    """Render the page explaining how to build language agents."""
    return render_template('building_agents.html')

@app.route('/hands-on-lab')
def hands_on_lab():
    """Render the page with interactive exercises."""
    return render_template('hands_on_lab.html')

@app.route('/resources')
def resources():
    """Render the page listing additional resources."""
    return render_template('resources.html')

@app.route('/submit-code', methods=['POST'])
def submit_code():
    """Handle code submissions from the hands-on exercises."""
    code = request.form.get('code')

    # Validate the code
    errors = validate_code(code)

    if errors:
        # Return the errors to the user
        return render_template('hands_on_lab.html', errors=errors)

    else:
        # Run the code
        output = run_code(code)

        # Return the output to the user
        return render_template('hands_on_lab.html', output=output)

# Define the code validation function
def validate_code(code):
    """Validate the given code."""
    errors = []

    # Check for proper references to all variables used in the HTML files
    for variable in ['name', 'age', 'city']:
        if variable not in code:
            errors.append(f"Variable {variable} not found in code.")

    return errors

# Define the code execution function
def run_code(code):
    """Run the given code."""
    output = subprocess.run(code, shell=True, stdout=subprocess.PIPE)
    return output.stdout.decode('utf-8')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
