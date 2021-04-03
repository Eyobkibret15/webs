from flask import Flask , render_template,request,redirect
app = Flask(__name__)
import csv

@app.route('/<path:subpath>')
def hello_world(subpath=None):
        if subpath == "send":
            return render_template("index.html")
        else:
            return render_template(subpath)
@app.route('/')
def tryi():
    return render_template("try.html")

# def database(data):
#     name = data["name"]
#     email = data["email"]
#     password = data["pass"]
#     with open('database.csv', 'a') as file:
#         file.write(name)
#         file.write(email)
#         file.write(password)

def databasecsv(data):
    name = data["name"]
    email = data["email"]
    password = data["pass"]
    with open('database.csv', newline='' ,mode= 'a') as file:

        fieldnames = ['name', 'email','password']
        writer =csv.writer(file, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow()
        print(name,email,password)
        writer.writerow([name,email,password])


@app.route('/', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        data = request.form.to_dict()
        databasecsv(data)
        return render_template("thanks.html")
    else:
        error = "invalid data"
        return error
    # the code below is executed if the request method
    # was GET or the credentials were invalid

#
# @app.route('/index.html')
# def home():
#     return render_template("index.html")
#
# @app.route('/generic.html')
# def generic():
#     return render_template("generic.html")
#
# @app.route('/landing.html')
# def landing():
#     return render_template("landing.html")
#
# @app.route('/elements.html')
# def elements():
#     return render_template("elements.html")
#
#
# @app.route('/favicon.ico')
# def fav():
#     return send_from_directory('static','favicon.ico')