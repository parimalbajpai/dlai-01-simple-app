from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the input form
@app.route('/')
def home():
    return render_template('index.html')

# Route to generate the card
@app.route('/generate', methods=['POST'])
def generate_card():
    # Get data from the form
    name = request.form.get('name')
    age = request.form.get('age')
    date = request.form.get('date')
    message = request.form.get('message')

    # Send this data to the card template
    return render_template('card.html', name=name, age=age, date=date, message=message)

if __name__ == '__main__':
    app.run(debug=True)