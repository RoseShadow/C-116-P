# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Stuti" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father") 
def father(): 
    name = "Vicktor" 
    age = "40" # write your age 
    
    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage

@app.route("/mother") 
def mom(): 
    name = "Babita" 
    age = "38"  
    
    return render_template('mother.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/friends") 
def mom(): 
    name = "Leksha" 
    age = "13"  
    
    return render_template('friend.html' , name = name , age = age)


# add other routes, if you want

@app.route("/friends") 
def mom(): 
    name = "Manya" 
    age = "14"  
    
    return render_template('friend.html' , name = name , age = age)

@app.route("/friends") 
def mom(): 
    name = "Mishti" 
    age = "14"  
    
    return render_template('friend.html' , name = name , age = age)




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
