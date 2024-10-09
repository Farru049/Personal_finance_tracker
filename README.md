# Personal Finance Tracker

## Flowchart

Here is the flowchart illustrating the workflow of the Personal Finance Tracker project:

![Flowchart](personal_finance_tracker/project flow/png)  <!-- Ensure the path is correct -->

![Project Logo](static/images/backgroundimage.jpg) <!-- Ensure the path is correct -->

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Visualizations](#visualizations)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The **Personal Finance Tracker** is a web application designed to help users manage and visualize their personal expenses effectively. This project allows users to upload their expense data in CSV format and provides insightful visualizations to analyze their spending habits.

## Features

- **User-friendly Dashboard**: Intuitive interface for uploading expense data.
- **Data Visualization**: Generate pie charts, bar charts, line charts, and histograms to visualize spending.
- **Monthly Expense Tracking**: View total expenses categorized by month.
- **Distribution Analysis**: Understand expense distribution with histograms.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Data Analysis**: Pandas, Matplotlib, Seaborn
- **Database**: CSV files for data storage
- **Version Control**: Git

## Installation

To set up the Personal Finance Tracker locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Farru049/Personal_finance_tracker.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Personal_finance_tracker
    ```

3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/dashboard`.

3. Upload your expense data in CSV format. The expected format is:
    ```
    Date,Category,Amount
    2024-01-01,Food,50
    2024-01-02,Transport,20
    ```

4. View the generated visualizations on the dashboard.

## Visualizations

The application generates the following visualizations based on uploaded data:

- **Pie Chart**: Displays the breakdown of expenses by category.
- **Bar Chart**: Shows total expenses per month.
- **Line Chart**: Tracks expenses over time.
- **Histogram**: Visualizes the distribution of expenses.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/YourFeature
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add some feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature/YourFeature
    ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, feel free to reach out:

- **Name**: Mohammad Farhaan Ali
- **Email**: alifarhaan655@gmail.com
- **LinkedIn**: [linkedin.com/in/farhaan-ali](https://linkedin.com/in/farhaan-ali)
- **GitHub**: [github.com/Farru049](https://github.com/Farru049)

# Personal_finance_tracker
