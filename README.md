# Flask Data Management Project

[![License](https://img.shields.io/badge/license-MIT-blue.svg)]
(https://opensource.org/licenses/MIT)

This project is a Flask web application that utilizes a data parser to retrieve random people's data from a third-party API. It provides a user interface to view and interact with this data.

## Requirements

- Python 3.x
- Flask
- SQLite 3

## Installation

1. Clone this repository to your local machine using:

git clone https://github.com/XRN-wq/flask.git


## Usage

1. Run the Flask application using:

python flask_app.py

2. Access the application by opening a web browser and navigating to `http://localhost:5000`.

3. Use the different routes to manage the data:
- `/` - Home page
- `/list` - View a list of data
- `/get` - Retrieve specific data using the API
- `/delete` - Delete data entries

## Data Parsing

The data parsing functionality is contained in a separate script. To use it:

1. Navigate to the `db` directory:

cd ..

cd db

2. Run the parser script:

python parser.py

## Testing

To run the unit tests, execute the following command:

python -m unittest test_app.py

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.