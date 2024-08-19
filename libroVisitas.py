from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
guestbook_entries = []

@app.route('/')
def index():
    return render_template('index.html', entries=guestbook_entries)

@app.route('/sign', methods=['POST'])
def sign_guestbook():
    name = request.form.get('name')
    message = request.form.get('message')
    guestbook_entries.append({'name': name, 'message': message})
    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
def clear_guestbook():
    guestbook_entries.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
