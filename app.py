from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('organizer-login.html')

@app.route('/login', methods=['POST'])
def process_input():
  # Retrieve the user's input from the form data
  user_input = request.form['secretkey']
  # Render the template to display the processed data
  return render_template('organizer-event.html', data=user_input)

@app.route('/create-event')
def create_event():
    return render_template('create-event.html')

if __name__ == '__main__':
    app.run(debug=True)