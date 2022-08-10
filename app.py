
from flask import Flask, render_template, request,  redirect
from peewee import *
from models import Register


app = Flask(__name__)

@app.route('/')
def qwe():
    all_users=Register.select()
    return render_template("index.html", users = all_users)





@app.route('/create/', methods=('GET', 'POST'))
def create():
    # l, u, p, d = 0, 0, 0, 0
    if request.method == 'POST':
        # if len(request.form['password']) >= 8:
        #     for i in request.form['password']:
        #         if (i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        #             l+=1 

        #         if (i in 'abcdefghijklmnopqrstuvwxyz'):
        #             u+=1

        #         if (i in '1234567890'):
        #             d+=1

        #         if(i in '!@#$%^&*()-+'):
        #             p+=1 
        # if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(request.form['password'])):
            Register.create(
                user_name = request.form['user_name'],
                password = request.form['password'],
                post = request.form['post'],
                email= request.form['email'] )
            return redirect('/')
        # print('Вы успешно зарегестрированы')

        # else:
        #     return render_template('create.html'),'Пароль должен быть длиннее 8 символов и содержать символ, цифру, большую и прописную буквы❗️'

        # return "Вы успешно зарегистрировались!"
        
    return render_template('create.html')



if __name__ == "__main__":
    app.run(debug = True)




    

