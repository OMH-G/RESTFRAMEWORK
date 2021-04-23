from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///ToDo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Todolist(db.Model):
    s=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self)-> str:
        return f"{self.s} - {self.title}"

@app.route('/',methods=['GET','POST'])
def HomePage():
    if(request.method=='POST'):
        title=request.form['title']
        desc=request.form['desc']
        todo=Todolist(title=title,desc=desc)
        if(todo.title not in Todolist.query.all() and todo.desc not in  [i.desc for i in Todolist.query.all()] and str(todo.title).strip()!='' and str(todo.desc).strip()!=''):
            db.session.add(todo)
            db.session.commit()
    alltodo=Todolist.query.all()
    return render_template('index.html',All_ToDo=alltodo)

@app.route('/delete/<int:s>')
def delete(s):
    alltodo=Todolist.query.filter_by(s=s).first()
    db.session.delete(alltodo)
    db.session.commit()
    # return render_template('index.html',All_ToDo=Todolist.query.all())
    return redirect('/')
@app.route('/update/<int:s>',methods=['GET','POST'])
@app.route('/update/<int:s>')
def update(s):
    if(request.method=='POST'):
        title=request.form['title']
        desc=request.form['desc']
        todo=Todolist.query.filter_by(s=s).first()
        todo.title=title
        todo.desc=desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    alltodo=Todolist.query.filter_by(s=s).first()
    return render_template('update.html',alltodo=alltodo)
if __name__=="__main__":
    app.run(debug=True,port=8000)