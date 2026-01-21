from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "change-me-to-a-secure-random-key"


@app.route('/')
def index():
    profile = {
        'name': 'Your Name',
        'title': 'Software Engineer',
        'bio': 'A short bio about you. Replace this with your own text.'
    }
    featured = [
        {'title': 'Project One', 'summary': 'Short description', 'url': url_for('projects')},
        {'title': 'Project Two', 'summary': 'Short description', 'url': url_for('projects')},
    ]
    return render_template('index.html', profile=profile, featured=featured)


@app.route('/projects')
def projects():
    projects_list = [
        {'title': 'Project One', 'description': 'Longer description', 'link': '#'},
        {'title': 'Project Two', 'description': 'Longer description', 'link': '#'},
    ]
    return render_template('projects.html', projects=projects_list)


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # In a real app you'd send an email or store the message.
        flash('Thanks for your message, we will get back to you soon!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
