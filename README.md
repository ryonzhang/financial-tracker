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

## Accessing the Deployed Endpoint

You can access the deployed endpoint by clicking on the following link:
[https://oyster-app-xcrss.ondigitalocean.app/report](https://oyster-app-xcrss.ondigitalocean.app/report)

## Assumptions
The Financial Tracker application operates based on certain assumptions to ensure its functionality and user experience. It is important to be aware of these assumptions when using the application:

1. **CSV Format for Transaction Data**: The application assumes that users will provide financial transaction data in CSV (Comma-Separated Values) format. Each line of the CSV data should include the date of the transaction, the type of the transaction, the amount, and an optional memo or description.

2. **Supported Transaction Types**: Financial transactions are categorized into two types: "Income" and "Expense." The application assumes that all transactions will fall into one of these two categories. Transactions with other types are considered invalid.

3. **Date Format and Validity**: Dates provided in transaction data should adhere to the "YYYY-MM-DD" format (e.g., "2020-12-01"). The application also assumes that dates are valid within the Gregorian calendar. Invalid dates, such as specifying a month outside the range of 1-12, will result in errors.

4. **Database Configuration**: Users are expected to configure and set up a PostgreSQL database to store transaction data and financial aggregates. Database connection details, such as the username, password, host, and database name, must be accurately configured in the code for proper database interaction.

5. **Financial Aggregate "AGGREGATE_ID"**: The code defines a constant value, "AGGREGATE_ID," as the identifier for the financial aggregate in the database. This identifier is used to maintain a single aggregate record that summarizes the financial data. The application assumes that this identifier remains consistent and accurate.

6. **Tallying Transactions**: When calculating the total gross revenue, expenses, and net revenue, the application assumes that the initial financial aggregates in the database are set to zero. Subsequent transactions are used to update these aggregates.

7. **Errors and Exception Handling**: The application assumes that errors and exceptions may occur during data input and processing. It provides error messages and exceptions to help users identify and rectify issues. Users are expected to handle and address any errors that may arise during the use of the application.

8. **All or Nothing CSV Record Insertion**: The application follows an "all or nothing" approach for CSV record insertion. If any record within a CSV file is invalid or contains errors, the entire CSV file will be rejected. This is done to maintain data consistency and integrity in the database.

## Limitations and Future Improvements:
1. **Limited User Management**: The application does not currently offer user management features, such as user accounts and authentication. As a result, all users share the same data, which can be a security and privacy concern.

2. **Error Handling**: While the application provides error messages for certain issues, the error handling and reporting could be more user-friendly and informative. Users may encounter cryptic error messages, making it challenging to identify and resolve issues.

3. **No Data Validation for Memo**: The application does not validate the format or content of the memo field, which means that users can enter any text without restrictions. This can lead to inconsistencies in memo data.

4. **Scalability**: The application may face scalability challenges as the volume of data increases. Handling a large number of transactions and generating reports for extended periods could impact performance.

5. **Lack of Data Backup**: There is no built-in data backup or recovery mechanism. If data is accidentally deleted or lost, there is no easy way to recover it.

6. **Single Aggregate Record**: The application relies on a single aggregate record to summarize financial data. While this approach simplifies data management, it may not be sufficient for complex financial analysis, especially when multiple financial entities are involved.

7. **Limited Reporting Customization**: The application's reporting feature provides basic financial reports, but users have limited flexibility to customize the structure and content of these reports to suit their unique needs.
