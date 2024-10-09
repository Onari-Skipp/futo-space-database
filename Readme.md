# SarahDB Flask Project

This project is a Flask-based web application that uses a custom dictionary-based database (DictDB) for data storage and management. It provides a simple API for CRUD operations on various models.

## Features

- Custom dictionary-based database 
- Flask web application with API endpoints
- User authentication and authorization
- Model management with schema support
- Encryption for data security

## Project Structure

- `main.py`: Entry point of the application
- `__init__.py`: Flask application initialization
- `views.py`: API route definitions
- `dictdb.py`: Custom database implementation
- `encrypt.py`: Encryption utilities

## Prerequisites

- Python 3.7+
- Flask
- Flask-SQLAlchemy
- Flask-Login

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/DavidNzube101/SarahDB.git
   cd SarahDB
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
   
4. Create necessary directories:
   ```
   mkdir -p instance/_io/models/model_settings
   ```

## Configuration

1. Update the `SECRET_KEY` in `__init__.py`:
   ```python
   app.config['SECRET_KEY'] = 'your-secret-key'
   ```

2. Set the `PRODUCTION` flag in `dictdb.py` to `True` if deploying to a production environment.

## Running the Application

1. Start the Flask development server:
   ```
   python main.py
   ```

2. Access the application at `http://localhost:781`

## Deploying to a Server

1. Set up a production-ready web server like Gunicorn or uWSGI.

2. Configure your web server to serve the Flask application.

3. Set up a reverse proxy (e.g., Nginx) to forward requests to your application server.

4. Ensure all necessary directories and files have the correct permissions.

5. Set up environment variables for sensitive information (e.g., SECRET_KEY).

6. Configure your firewall to allow traffic on the necessary ports.

7. Set up SSL/TLS for secure communications.

## API Endpoints

- `/`: Home page
- `/handler`: Requires login
- `/<api_email>/<api_password>/<api_key>/handler`: Get all model data
- `/<api_email>/<api_password>/<api_key>/handler/get_all/<model>`: Get all entries for a specific model
- `/<api_email>/<api_password>/<api_key>/handler/find_all/<model>/<column>/<value>`: Find all entries in a model where a column matches a value
- `/<api_email>/<api_password>/<api_key>/handler/add_one/<model>/<column>/<item>`: Add a new entry to a model
- `/<api_email>/<api_password>/<api_key>/handler/add_entry`: Add a new entry to a model (POST request)
- `/<api_email>/<api_password>/<api_key>/handler/find_one/<model>/<column>/<item>`: Find one entry in a model
- `/<api_email>/<api_password>/<api_key>/handler/update_one/<model>/<column>/<item_search>/<item_update>`: Update an entry in a model
- `/<api_email>/<api_password>/<api_key>/handler/update_entry/<model>/<column>/<column_value_pair>`: Update an entry in a model
- `/<api_email>/<api_password>/<api_key>/handler/update_entry_dnd`: Update an entry in a model (POST request)
- `/<api_email>/<api_password>/<api_key>/handler/delete_entry/<model>/<column>`: Delete an entry from a model

  i'd drop the Databse client soon.....anticipate

## Security Considerations

- Always use HTTPS in production
- Regularly update dependencies
- Use strong, unique passwords for API access
- Implement rate limiting to prevent abuse
- Regularly backup your data

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
