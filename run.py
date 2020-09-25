import os

from app import create_app

# config_name = os.getenv('APP_SETTINGS')  # config_name = "development"
# The above isn't working, so hard coding it for now
# Looks like the .envrc file is not working
# Trying out dotenv instead
# config_name = 'development'
app = create_app()

if __name__ == '__main__':
    app.run()
