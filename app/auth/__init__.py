from flask import Blueprint

auth = Blueprint('auth',__name__)

from . import views
from . import views,forms


#@auth.route('/login')
#def login():
    #return render_template('auth/login.html')