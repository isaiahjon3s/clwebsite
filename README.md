# CantiLever Solutions Website

A modern Flask website for CantiLever Solutions—custom PCB design for microscopes and specialized applications.

## Features

- **Landing Page** — High-quality hero with PCB imagery, features, and portfolio gallery
- **Products** — Services overview: microscope control boards, sensing electronics, prototyping, DFM, consulting
- **About** — Company background, capabilities, and expertise
- **Contact** — Inquiry form with project type selection and flash message feedback

## Setup

```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the development server
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Production

- Set a strong `SECRET_KEY` in app configuration
- Configure a production WSGI server (e.g., Gunicorn)
- Add email backend for contact form submissions

## Images

PCB and electronics imagery is sourced from Unsplash. Replace with your own assets in `static/images/` and update template references as needed.
# clwebsite
