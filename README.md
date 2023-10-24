# Financial Tracker

## Overview

Financial Tracker is a Python application that enables users to manage financial transactions and generate reports. It provides a RESTful API for adding, viewing, deleting transactions, tallying transactions, and generating financial reports.

## Installation
1. Install Dependencies:\
`pip install -r requirements.txt`
2. Database Configuration:\
Configure a PostgreSQL database, replacing the database information in the db.bind() call with your own database details.
3. Start the Database\
`python db.py`
4. Start the App\
`waitress-serve --port=8080 --call app:create_app`

## Dockerization
1. Build the Docker Image\
`docker build . -t transaction_server`
2. Run the Transaction Container
`docker run -p 8080:8080 transaction_server`

## Tests
### Prerequisites
Before running the test cases, make sure that you have the project and its dependencies set up. You can follow the installation instructions provided in the project's README.

### Running the Test Cases
To run the test cases, execute the following command in your project directory:
`pytest -v`\
The -v flag is used for verbose output, which provides more detailed information about the test results.

### Test Cases
1. Initialize the Database\
   This test initializes the database to ensure that it is empty and ready for testing.

2. Get Report with Empty Data\
   This test checks if the generated financial report is correct when no transactions are present.

3. Post Transactions with Incorrect Header\
   This test verifies that posting transactions with an incorrect header results in an error message.

4. Post Transactions Successfully\
   This test checks if transactions are added successfully, and the financial report is updated accordingly.

5. Post Transactions with Incorrect Data\
  These tests validate that the application handles incorrect data entries in transactions correctly.

6. Post Multiple Transactions Successfully\
   This test verifies that multiple transactions are added successfully, and the financial report reflects the correct calculations.

These test cases cover various aspects of the Financial Tracker application, including initialization, adding transactions, handling incorrect data, and generating financial reports. Running these tests will help ensure the application's correctness and robustness.

## API

The Financial Tracker API supports the following actions:

- **Add Transactions**
    - **Endpoint:** `/transactions`
    - **Method:** `POST`
    - **Content-Type:** `text/csv`
    - **Description:** Add financial transactions in CSV format.

- **Get Transactions**
    - **Endpoint:** `/transactions`
    - **Method:** `GET`
    - **Description:** Retrieve a list of all financial transactions.

- **Delete Transaction**
    - **Endpoint:** `/transactions/<transaction_id>`
    - **Method:** `DELETE`
    - **Description:** Delete a specific financial transaction by providing its ID.

- **Tally Transactions**
    - **Endpoint:** `/tally`
    - **Method:** `GET`
    - **Description:** Calculate the total gross revenue, expenses, and net revenue based on all transactions.

- **Generate Report**
    - **Endpoint:** `/report`
    - **Method:** `GET`
    - **Description:** Generate a financial report, including gross revenue, expenses, and net revenue.
