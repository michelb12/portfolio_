from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
print(__name__)
'''
@app.route('/<username>/<int:post_id')
def hello_world(name=None, post_id=None):
    return render_template('index.html', name=name, post_id=post_id)
    '''
@app.route('/index.html')
def my_home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/works.html')
def works():
    return render_template('works.html')


@app.route('/work.html')
def work():
    return render_template('work.html')




@app.route('/contact.html')
def contact():
    return render_template('contact.html')


""" 
@app.route('/favicon.ico')
def about():
    return render_template('about.html')
 """



@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_login():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_txt_file(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong try again'

def write_to_txt_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')
