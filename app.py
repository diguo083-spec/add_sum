from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def add_sum(n1):
    total = 0
    for i in range(1, n1 + 1):
        total += i
    return total

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sum', methods=['POST'])
def calc_sum():
    data = request.get_json()
    n = int(data['n'])

    if n < 1:
        return jsonify({'error': 'n必须大于等于1'}), 400

    result = add_sum(n)
    return jsonify({
        'n': n,
        'result': result
    })

if __name__ == '__main__':
    app.run(debug=True)