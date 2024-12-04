from flask import Flask, request, jsonify, render_template
from linked_list import LinkedList

app = Flask(__name__)

linked_list = LinkedList()

@app.route('/')
def index():
    return render_template('project/template/index.html')

@app.route('/add', methods=['POST'])
def add_node():
    data = request.form['data']
    linked_list.append(data)
    return jsonify({'status': 'success', 'list': linked_list.display()})

@app.route('/remove_beginning', methods=['POST'])
def remove_beginning():
    removed_data = linked_list.remove_beginning()
    return jsonify({'removed': removed_data, 'list': linked_list.display()})

@app.route('/remove_at_end', methods=['POST'])
def remove_at_end():
    removed_data = linked_list.remove_at_end()
    return jsonify({'removed': removed_data, 'list': linked_list.display()})

@app.route('/remove_at', methods=['POST'])
def remove_at():
    data = request.form['data']
    removed_data = linked_list.remove_at(data)
    return jsonify({'removed': removed_data, 'list': linked_list.display()})

@app.route('/display', methods=['GET'])
def display_list():
    return jsonify({'list': linked_list.display()})

if __name__ == '__main__':
    app.run(debug=True)
