from flask import Flask, request, render_template, redirect, url_for
import os
import pandas as pd
from visualizations import generate_visualizations  # Import the visualizations module

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['VISUAL_FOLDER'] = './static/visualizations'

# Ensure folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['VISUAL_FOLDER'], exist_ok=True)

# Load data from the uploaded file
def load_data(file_path):
    expenses_df = pd.read_csv(file_path)

    # Assuming there's a 'Date' column in the CSV to extract month
    expenses_df['Date'] = pd.to_datetime(expenses_df['Date'])  # Adjust the column name as necessary
    expenses_df['Month'] = expenses_df['Date'].dt.month_name()  # Extract month name
    
    return expenses_df

# Redirect the home route to the dashboard
@app.route('/')
def home():
    return redirect(url_for('dashboard'))  # Redirect to the dashboard

# Route for the dashboard (file upload)
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Load data and generate visualizations
            expenses_df = load_data(file_path)
            pie_chart_path, bar_chart_path, line_chart_path, histogram_path = generate_visualizations(expenses_df)

            return redirect(url_for('view_data', pie_chart=pie_chart_path, bar_chart=bar_chart_path,
                                    line_chart=line_chart_path, histogram=histogram_path))
    return render_template('dashboard.html')

# Route for displaying the visualized data
@app.route('/view_data')
def view_data():
    pie_chart = request.args.get('pie_chart')
    bar_chart = request.args.get('bar_chart')
    line_chart = request.args.get('line_chart')
    histogram = request.args.get('histogram')

    return render_template('view_data.html', pie_chart=pie_chart, bar_chart=bar_chart,
                           line_chart=line_chart, histogram=histogram)

if __name__ == '__main__':
    app.run(debug=True)
