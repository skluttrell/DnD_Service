# DnD_Service
Web interface, database, and server tools for storing and maintaining Dungeons and Dragons character and session data

# Goals
To provide a service for storing and maintaining D&D information accessible to users with disabilities (Character and sessions)
Provide mechanisms for tracking games, session notes, characters, players, and any other useful data
Provide an interface for hosting a session (Dungeon Master tools)
Provide a web interface that is accessible to all users

# Installation and usage
This project requires various packages found in the requirements.txt file

This project uses Python 3.75 and Flask

=====
Flask
=====

# From the website
Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.
Flask offers suggestions, but doesn't enforce any dependencies or project layout. It is up to the developer to choose the tools and libraries they want to use. There are many extensions provided by the community that make adding new functionality easy.
--> https://palletsprojects.com/p/flask/

# Setting up a python virtual environment
It is strongly suggested that you work in a virtual environment to protect your main Python installation or to be granted modification rights if you are not an administrator.

# For Python > v3.4
$ Python -m venv venv

# for Python < v3.4
The package "virtualenv" is required to create virtual environments.
Once it is installed, the command to create a virtual environment is:
$ virtualenv venv

# To activate the virtual environment
# On Windows command line
$ venv\Scripts\activate (venv) $ _
# Everyone else
$ source venv/bin/activate

# Installing project dependencies
pip install -r requirements.txt

# Running the Flask server
$ flask run

# Accessing the web interface via a web browser
http://localhost:5000/<domain>

# Domains
Domains are found in the app/routes.py file.

Examples:
@app.route('/')
@app.route('/index')
@app.route('/spell/<name>') --> Where name is the name of a spell such as "acid_arrow"

# Further reading
The Flask Mega-Tutorial by Miguel Grinberg: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

=====================
Files and Directories
=====================

app --> Directory
app/templates --> Directory of Jinya2 templates
app/templates/_class_table.html --> Template for arranging the information by level found in a character class table
app/templates/_spell.html --> Template for arranging individual spell information
app/templates/base.html --> Main template for all webpage formatting
app/templates/character.html --> Template for arranging individual character information
app/templates/class.html --> Template for arranging individual class information
app/templates/edit_character.html --> Template which provides a web interface to edit an individual character's data such as for leveling
app/templates/index.html --> Template for the home page
app/templates/list_of_spells.html --> Template for arranging a list of all spells by name
app/templates/new_character.html --> Template for creating a new character
app/templates/test.html --> A test page
app/__convert.py --> Converts plain text with meta tags to html
app/__get_data.py --> Gives Jquery post calls access to the main database
app/__init__.py --> Required Flask file: initializes the Flask server
app/forms.py --> Defines form elements for use on web form templates
app/models.py --> Defines models to build SQL databases
app/routes.py --> Defines functions to be performed when domains are accessed
Migrations --> Directory Flask initializes as part of the process of building databases (Keeps track of database changes)
notes --> Directory for storing project notes
tests --> Directory for storing various project unit tests
1_origins.py ... 12_eldritch_invocations.py --> Sequenced files for automatically populating the database
app.db --> The database file in SQLite
config.py --> Defines Flask configuration variables
requirements.txt --> Pip generated dependencies file