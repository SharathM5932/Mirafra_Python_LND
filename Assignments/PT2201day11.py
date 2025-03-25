# # flask- WSGI is a universal framework for client and server
# # In flask we use wesk--_ wsgi
# @app.route('/')
# def home():
#     return "hello world"
#
# # if <name> any name can be written then the argu should also be given
# # @app.route('/<number>')
# # def index1(number):
# #     if int(number)%2==0:
# #         return "<h1>"even"<h2>"
# #     else:
# #         return "odd"
#
# # if <int:number> then we have to give integer like str, float
# @app.route('/<int:number>')
# def index1(number):
#     if int(number)%2==0:
#         return "<h1>even<h2>"
#     else:
#         return "odd"
#
# # passing parameters from one function to other taken from url
# @app.route('/anuroop/<number>')
# def new(number):
#     return redirect(url_for('index1',number=number))