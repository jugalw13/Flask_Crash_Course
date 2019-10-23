from flask import current_app as app
from flask import jsonify, request

from todo_app import db
from todo_app.models import TODO

@app.route("/todo/add-item", methods=['POST'])
def add_item():
    if request.method == 'POST':
        text = request.data.decode('utf-8')
        s = TODO(text=text)
        db.session.add(s)
        db.session.commit()
        if s.id == None: 
                return jsonify({"result: failure"})
        return jsonify({"result":"success"})

@app.route("/todo/get-list", methods=['GET'])
def get_item():
    if request.method == 'GET':
        text = "I will do it today"

        return jsonify(text)