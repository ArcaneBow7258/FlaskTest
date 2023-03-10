from flask import Flask
# EB looks for an 'application' callable by default.
application = Flask(__name__)

# print a nice greeting.
@application.route('/',methods=['GET','POST'])
def index():
    return  '<p>Hello %s!</p>\n'



# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
