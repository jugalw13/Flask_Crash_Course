import json

from flask import current_app as app
from flask import jsonify, request

from todo_app import db
from todo_app.models import TODO


@app.route("/todo/add-list", methods=['POST'])
def add_item():
    text = ""
    todo = None
    try:
        data = request.get_json()
        text = data['text']
        todo = TODO(text=text)
        db.session.add(todo)
        db.session.commit()
    except Exception:
        pass

    if todo is None: 
            return jsonify({"result: failure"})
    return jsonify({"result":"success"})

@app.route("/todo/get-list", methods=['GET'])
def get_item():
    result = None
    result = TODO.query.all()
    if result is None:
        return jsonify(f"error: Invalid ID: {id}")
    result = [r.__dict__ for r in result]
    for i in result:
        del i['_sa_instance_state']
    return jsonify(result)

@app.route("/todo/update-list", methods=['PUT'])
def put_item():
    todo, id, text = None, None, None
    try:
        data = request.get_json()
        id = int(data['id'])
        text = data['text']
        todo = TODO.query.get(id)
        todo.text = text
        db.session.add(todo)
        db.session.commit()
    except Exception:
        pass
    
    if todo is None:
        return jsonify(f"error: Invalid data ID: {id}, text: {text}")
    return jsonify(f"updated: id={todo.id}")

@app.route("/todo/delete-list", methods=['DELETE'])
def del_list():
    result, id = None, None
    try:
        data = request.get_json()
        id = int(data['id'])
        result= TODO.query.get(id)
        db.session.delete(result)
        db.session.commit()
    except Exception:
        pass
    
    if result is None:
        return jsonify(f"error: Invalid data ID: {id}")
    return jsonify(f"Deleted: id={result.id}")