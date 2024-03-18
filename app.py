from flask import Flask, render_template

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
