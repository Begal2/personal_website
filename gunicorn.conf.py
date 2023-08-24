# Gunicorn config file

# Command to run Gunicorn
command = '/Users/tingyuwang/anaconda3/bin/gunicorn'

# Number of worker processes
workers = 4

# Address and port to bind
bind = '0.0.0.0:8000'

# The application module to import
# Change 'server' to the name of your Flask app file (without the '.py' extension)
# For example, if your Flask app is in a file named 'app.py', then set this to 'app'
app_module = 'server'

# Application callable within the specified module
# This should be the Flask app instance
app_callable = 'app'

