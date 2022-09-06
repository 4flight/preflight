
from distutils.command.config import config
from distutils.file_util import write_file
from distutils.log import debug
from flask import Flask ,render_template , redirect , url_for, session, request
from flask_wtf.csrf import CSRFProtect 
from config import config , NameForm
from flask_mysqldb import MySQL 
from wtforms.validators import Required
 



app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    """ form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        
    return redirect(url_for('index'))
    return render_template('main.html', form=form, name=session.get('name')) """
    #return render_template('./main.html')

@app.route('/edit/', methods = ['POST', 'GET'])
def get_airport(name):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM aiports_table WHERE name = %s', (name))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-contact.html', contact = data[0])

def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return render_template('error_page/404.html'),404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(debug=True,port= 5000)
    
    
