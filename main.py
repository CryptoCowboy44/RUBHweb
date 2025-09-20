from flask import Flask, render_template, send_from_directory
import mimetypes

# Register common video MIME types
mimetypes.add_type('video/mp4', '.mp4')
mimetypes.add_type('image/gif', '.gif')

from app import app  # noqa: F401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)