from flask import Flask, render_template, request

app = Flask(__name__)

# Simple function for prediction (replace with actual ML model)
def predict(data):
    return f"Predicted Value: {float(data) * 2:.2f}"

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        input_value = request.form.get('input_value')
        if input_value:
            result = predict(input_value)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
