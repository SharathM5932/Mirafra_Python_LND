from flask import Flask, abort
import re

app = Flask(__name__)

@app.route('/rev/<revstr>')
def reverse_string(revstr):
    if not re.match(r'^[a-zA-Z]+$', revstr):
        abort(400, "Invalid format. Only letters are allowed.")
    return f"Reversed string: {revstr[::-1]}"

if __name__ == '__main__':
    app.run(debug=True)