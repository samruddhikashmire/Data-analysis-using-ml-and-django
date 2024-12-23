# Data-analysis-using-ml-and-django

This project is a simple web-based CSV analyzer built with Django. It allows users to upload a CSV file and provides insights such as:

- A preview of the first few rows of the dataset.
- Summary statistics for numerical columns.
- Details about missing values.
- A heatmap visualization of the correlation between columns.

## Features

1. **File Upload**: Users can upload CSV files directly from their browser.
2. **Data Preview**: The first few rows of the dataset are displayed in an HTML table.
3. **Summary Statistics**: Provides statistical details like mean, median, standard deviation, etc.
4. **Missing Values**: Displays the count of missing values for each column.
5. **Correlation Heatmap**: Visualizes the correlation matrix using a heatmap.

## Requirements

- Python 3.11+
- Django 4.2.5
- Pandas
- Matplotlib
- Seaborn

## Installation Steps

1. **Clone the Repository**

   First, clone this repository to your local machine:

   ```bash
   git clone https://github.com/samruddhikashmire/Data analysis using ml and django.git
   
2. **Runserver**
   cd csv_analyzer
   python manage.py migrate
   python manage.py runserver
   
3. **Run the Development Serverr**
http://127.0.0.1:8000/


   
