#since we want to use templates, we have to import it now. 
from flask import render_template
from app import app
#Routes are the different URLS that the application implements.
@app.route('/')
#the decorators are the lines with @. A decorator modifies the function that follows it.
@app.route('/index')
def index():
    user = {'username' : 'William'}
    #Render converts a template into a complete HTML page called a rendering. This function takes a template filename and a vcariable list of template arguments and returns the same template but with all the placeholders in it replaced with actual values. 
    favorites = [
        {
            'author':{'username' : 'John'},
            'body' : 'Beautiul day in Portland'
        },
        {
            'author' : {'username' : 'Susan'},
            'body' : 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, favorites=favorites)

@app.route('/favorites')
def favorites():
    context ={
        'title': 'Favorites',
        'favorites' : ['The Power of Now by Eckhart Tolle' , "The Heart of the Buddha's Teaching: Transforming Suffering into Peace, Joy, and Liberation by Thich Nhat Hanh" , 'The Untethered Soul by Michael Singer' , 'The Four Agreements: A Practical Guide to Personal Freedom by Miguel Ruiz' , 'The Hobbit by Tolkien'],
    } 

    return render_template('favorites.html' , **context)
