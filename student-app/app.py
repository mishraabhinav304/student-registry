from flask import Flask, request, jsonify

app = Flask(__name__)

students = []

@app.route('/')
def home():
    return "Student Management API Running"

@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.json
    students.append(data)
    return jsonify({"message": "Student added successfully"}), 201

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)