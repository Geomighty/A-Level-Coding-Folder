from flask import Flask
from flask import request
from flask import render_template
import datetime as dt

app = Flask(__name__)

# @app.route('/add')
# def add():
#     first_number = request.args.get('first', '')
#     second_number = request.args.get('second', '')
#     if first_number and second_number:
#         try:
#             result = int(first_number) + int(second_number)
#         except ValueError:
#             return "Invalid input. Please provide two integers."
#         return f'{first_number} + {second_number} = {result}'
#     else:
#         return'No arguments detected'

# @app.route('/test')
# def test():
#     return "<h1>This is a test</h1><p>test<p>"

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def greet(name = ''):
#     return render_template('hello.html', name = name)

# @app.route('/hello/submit')
# def get_name():
#     return render_template('hello_submit_form.html')

# @app.route('/greet', methods = ['POST'])
# def greet():
#     typed_name = request.form['name']
#     print(typed_name)
#     return render_template('hello.html', name=typed_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)


@app.route('/birthday')
def birthday():
    year = request.args.get('year', '')
    month = request.args.get('month', '')
    day = request.args.get('day', '')
    dob = dt.date(int(year), int(month), int(day))
    today = dt.date.today()

    print("My date of birth is: ", dob)
    print("Today is: ", today)
    birthday_this_year = dt.date(today.year, dob.month, dob.day)
    birthday_next_year = dt.date(today.year+1, dob.month, dob.day)

    if birthday_this_year > today:
        next_birthday = birthday_this_year
    else:
        next_birthday = birthday_next_year

    print('Next birthday: ', next_birthday)
    days_to_birthday = (next_birthday - today).days
    age = (next_birthday - dob).days // 365
    print('Days to next birthday: ', days_to_birthday)
    print('Age at next birthday: ', age)