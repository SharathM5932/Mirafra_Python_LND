Step 1: Check if the Virtual Environment Exists
Go to your project directory in the terminal.
Look for a folder named venv. It should contain subfolders like Scripts or bin.
If the venv folder doesn't exist, create a virtual environment using:

python -m venv venv

PS C:\Users\Nagadeepthi MR\PycharmProjects\deepthi> python -m venv venv
PS C:\Users\Nagadeepthi MR\PycharmProjects\deepthi> venv\Scripts\activate
(venv) PS C:\Users\Nagadeepthi MR\PycharmProjects\deepthi> deactivate

pip install -r requirements.txt
.....................................
https://sqlitebrowser.org/dl/
....................................
easily install sqlite3
.........................
open database-> open your 'instance' folder(which is auto created) in the Python flask project. select data file to open the particular database.
choose->'Execute SQL' and write quires. write CRUD operation, commit and close the app.
after closing the sqlite app only run flask file again to see the changes else SQLite will lock the bd, changes cannot be seen. 
.............................
INSERT INTO user (name, email) VALUES ('Alice', 'alice@example.com');
SELECT * FROM user;
SELECT name, email FROM user;
SELECT * FROM user WHERE name = 'Alice';

UPDATE user
SET email = 'alice.new@example.com'
WHERE name = 'Alice';

DELETE FROM user WHERE name = 'Alice';

COMMIT


