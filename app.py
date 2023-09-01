from flask import Flask, render_template, request, redirect, url_for, send_file
import pandas as pd
import os
from openpyxl import load_workbook
from openpyxl.styles import PatternFill
import requests

app = Flask(__name__)

# Define the folder where uploaded files will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'xlsx'}

# Function to validate a UK postcode using Postcode.io API
def validate_uk_postcode(postcode):
    url = f"https://api.postcodes.io/postcodes/{postcode}/validate"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("result", False)
    return False

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        # Save the uploaded file with a new name, such as "sanitized_Filename.xlsx"
        new_filename = 'sanitized_Filename.xlsx'
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
        file.save(file_path)
        
        # Redirect to the processing route
        return redirect(url_for('process_file', filename=new_filename))
    
    else:
        return 'Invalid file format. Please upload an Excel file with .xlsx extension.'

@app.route('/process/<filename>')
def process_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    try:
        # Load the existing Excel file
        workbook = load_workbook(file_path)
        worksheet = workbook.active
        
        # Create a set to keep track of company names for checking duplicates
        company_names = set()
        
        # Iterate through rows and highlight duplicates
        for row in worksheet.iter_rows(min_row=2, max_row=worksheet.max_row, min_col=1, max_col=worksheet.max_column):
            company_col, postcode_col = row[0], row[1]
            
            # Check for duplicates in 'Name of Company' column and highlight in yellow
            if company_col.value in company_names:
                company_col.fill = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')
            else:
                company_names.add(company_col.value)
            
            # Check for incorrect postcodes and highlight in red
            if not validate_uk_postcode(postcode_col.value):
                postcode_col.fill = PatternFill(start_color='FF0000', end_color='FF0000', fill_type='solid')
        
        # Save the Excel file with styling
        workbook.save(file_path)
        
        # Send the processed Excel file as a response
        return send_file(file_path, as_attachment=True, download_name=filename)
    
    except Exception as e:
        return f'Error processing the file: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
