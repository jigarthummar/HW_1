from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/profile')
def home():
    return render_template('profile.html')  

@app.route('/contact')
def about():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)