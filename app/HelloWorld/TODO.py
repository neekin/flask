from flask_restful import reqparse,Resource,fields,marshal_with


TODOS={
  'todo1':{'task':1},
  'todo2':{'task':2},
  'todo3':{'task':3}
}

parser=reqparse.RequestParser()
parser.add_argument('task',type=int,required=True,help='Please set a int task content')

class Todo(Resource):
  def get(self,todo_id):  
      #todo_id = int(max(TODOS.keys()).lstrip('todo'))
      todo_id = 'todo'+todo_id
      print(TODOS[todo_id]) 
      return TODOS[todo_id],200

class TodoList(Resource):
  def get(self):
      return TODOS,200,{'Etag':'some-opaque-string'}
      
  def post(self):
      args = parser.parse_args()
      todo_id = int(max(TODOS.keys()).lstrip('todo'))+1
      todo_id = 'todo%i' % todo_id
      TODOS[todo_id] = {'task':args['task']}
      return TODOS[todo_id],201    
    
