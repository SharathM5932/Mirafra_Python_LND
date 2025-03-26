from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello():
    return "hello world"
@app.route('/<num>')
def cal(num):
    if int(num)%2==0:
        return "even"
    else:
        return "odd"


if __name__=='__main__':
    app.run(debug=True)