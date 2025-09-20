
import os
import logging
from flask import Flask, render_template, send_from_directory

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev_secret_key_change_in_production")

# Add route to serve files from attached_assets folder
@app.route('/attached_assets/<path:filename>')
def serve_asset(filename):
    """Serve files from the attached_assets folder."""
    try:
        return send_from_directory('attached_assets', filename)
    except Exception as e:
        logging.error(f"Error serving asset {filename}: {str(e)}")
        return "File not found", 404

@app.route('/')
def index():
    """Render the main page."""
    try:
        return render_template('index.html')
    except Exception as e:
        logging.error(f"Error rendering template: {str(e)}")
        return "Error loading page", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
