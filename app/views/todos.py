# coding: utf-8

from leancloud import Object, Query, LeanCloudError
from flask import Blueprint, request, redirect, url_for, render_template


class Todo(Object):
    pass


todos_view = Blueprint('todos', __name__)


@todos_view.route('')
def show():
    try:
        todos = Query(Todo).descending('createdAt').find()
    except LeanCloudError as e:
        if e.code == 101:  # 服务端对应的 Class 还没创建
            todos = []
        else:
            raise e
    return render_template('todos/todos.html', todos=todos)


@todos_view.route('', methods=['POST'])
def add():
    content = request.form['content']
    todo = Todo(content=content)
    try:
        todo.save()
    except LeanCloudError as e:
        return e.error, 502
    return redirect(url_for('todos.show'))
