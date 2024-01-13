from flask import Flask, request ,render_template , jsonify

app = Flask(__name__) # creates the Flask instance, __name__ is the name of the current Python module

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def math_ops():
    """
    Perform mathematical operations based on the user's input.
    Returns result based on users input and operation selected
    """
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtract of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiply of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The divide of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
            
        return render_template('results.html' , result = result)
    
@app.route('/postman_action',methods=['POST'])
def math_ops1():
    """
    Same as above, but for Postman (for testing purposes)
    """
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtract of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiply of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The divide of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
            
        return jsonify(result)

if __name__=="__main__": # checks whether this file is executed directly from the Python interpreter, and not used as an imported module
    app.run(host="0.0.0.0") # runs the application on the repl development server