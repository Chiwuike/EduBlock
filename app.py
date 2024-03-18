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
