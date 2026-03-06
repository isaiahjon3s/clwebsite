"""
CantiLever Solutions - Custom PCB Design
Flask Web Application
"""

from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'cl-solutions-secret-key-change-in-production'


@app.context_processor
def inject_now():
    return {'now': datetime.now}


@app.route('/')
def index():
    """High-quality landing page."""
    return render_template('index.html')


@app.route('/products')
def products():
    """Products and services page."""
    return render_template('products.html')


@app.route('/about')
def about():
    """About CantiLever Solutions."""
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page with inquiry form."""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        company = request.form.get('company', '').strip()
        project_type = request.form.get('project_type', '')
        message = request.form.get('message', '').strip()

        # Basic validation
        if not name or not email or not message:
            flash('Please fill in name, email, and message fields.', 'error')
            return redirect(url_for('contact'))

        # In production: send email, save to database, etc.
        flash('Thank you for your inquiry! We will respond within 24-48 hours.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
