#!env/bin/python

from app import app
import os

port = int(os.environ.get('PORT', 33507))
app.run(debug=False, host='0.0.0.0', port=port)