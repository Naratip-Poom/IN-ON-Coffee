# from flask import Flask, render_template, request, flash, session
# app = Flask (__name__)
# app.config['SECRET_KEY'] = 'asdfgh jklp'

# @app.route('/') 
# def home():
#     return render_template("home.html")

# @app.route('/login', methods=['POST', 'GET']) 
# def login(): 
#     return render_template("login.html")
    
# @app.route('/login1', methods=['POST', 'GET']) 
# def login1(): 
#     return redirect(url_for("login()"))

# @app.route('/success',methods=['POST' ])
# def success(): 
#     if request.method == 'POST' : 
#         session [ 'email'] = request.form['email'] 
#     return render_template("success.html")

# @app.route( '/logout')
# def logout():
#     if 'email' in session :
#         session.pop('email',None) 
#         return render_template("logout.html")
#     else : return render_template("login.html")

# @app.route('/profile')
# def profile():
#     if 'email' in session : 
#         email = session[ 'email'] 
#         return render_template("profile.html", email=email)
#     else : 
#         return render_template("login.html")

# if __name__ == "__main__" : 
#     app.run(debug=True)       