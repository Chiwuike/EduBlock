from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
