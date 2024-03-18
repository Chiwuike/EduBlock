from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
#Admin flask login:
app.secret_key = 'your_secret_key'  # Change this to a random secret key

login_manager = LoginManager()
login_manager.init_app(app)

# User model
class Admin(UserMixin):
    def __init__(self, id):
        self.id = id

# This would be replaced by your actual user loading mechanism, e.g., from a database
@login_manager.user_loader
def load_user(user_id):
    return Admin(user_id)

# Admin login route
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here you should verify the username and password
        # For simplicity, we'll assume any login is successful
        admin_user = Admin(username)
        login_user(admin_user)
        return redirect(url_for('admin_dashboard'))
    return render_template('admin_login.html')

# Admin dashboard route
@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # Retrieve courses from the database to display
    return render_template('admin_dashboard.html')

# Admin logout route
@app.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('home'))

# Run the application…


#Home page that lists all courses
@app.route('/')
def home():
    #In a real application, you would retrieve these from a database course = [
        {'title': 'Blockchain 101', 'description': 'Introduction to blockchain technology.'},
        {'title': 'Ethereum and Smart Contracts', 'description': 'Learn how to create smart contracts on Ethereum.'},
        {'title': 'Cryptocurrency Trading', 'description': 'Strategies for trading cryptocurrencies.'}
    ]
    return render_template('home.html', courses=courses)

#Course page that shows details about a specific course
@app.route('/course/<course_id>')
def course(course_id):
    #In a real application, you would retrieve this from a database using the course_id
    course = {
        'id': course_id,
        'title': 'Blockchain 101',
        'content': 'Here is some educational content about blockchain...'
    }
    return render_template('course.html', course=course)

if __name__ == '__main__':
    app.run(debug=True)
    
# Existing routes...

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Here you would handle the sign-up logic, such as saving the user data
        # For now, let's just redirect to the home page after sign-up
        return redirect(url_for('home'))
    return render_template('signup.html')

# Run the application…
from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your-database.db'
db = SQLAlchemy(app)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

# Route to add a new course
@app.route('/admin/course/new', methods=['GET', 'POST'])
@login_required
def add_course():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        new_course = Course(title=title, description=description)
        db.session.add(new_course)
        db.session.commit()
        return redirect(url_for('admin_dashboard'))
    return render_template('add_course.html')

# Route to edit an existing course
@app.route('/admin/course/edit/<int:course_id>', methods=['GET', 'POST'])
@login_required
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    if request.method == 'POST':
        course.title = request.form['title']
        course.description = request.form['description']
        db.session.commit()
        return redirect(url_for('admin_dashboard'))
    return render_template('edit_course.html', course=course)

# Route to delete a course
@app.route('/admin/course/delete/<int:course_id>', methods=['POST'])
@login_required
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return redirect(url_for('admin_dashboard'))

# Run the application...
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)


Courses db:

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Course {self.title}>'
from flask import Flask
from your_model_file import db, Course  # Assuming your models are in 'your_model_file.py'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()
