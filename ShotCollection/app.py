from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    
    # Do something with the data (e.g. store it in a database, send an email)
    
    response_data = {
        'status': 'success',
        'message': 'Form submitted successfully!'
    }
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run()