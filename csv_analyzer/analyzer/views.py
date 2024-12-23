from django.shortcuts import render
import pandas as pd
from .forms import FileUploadForm
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

def upload_file(request):
    if request.method == 'POST' and request.FILES['dataset']:
        file = request.FILES['dataset']
        df = pd.read_csv(file)  

        #first few rows 
        first_few_rows = df.head().to_html()

        #Check if specific columns exist
        if 'column_name' in df.columns:
            first_few_rows = df[['column_name']].head().to_html()

        #Summary statistics
        summary_statistics = df.describe().to_html()

        #Missing values
        missing_values = df.isnull().sum()  # Series
        missing_values_df = missing_values.reset_index()
        missing_values_df.columns = ['Column', 'Missing Values']
        missing_values_html = missing_values_df.to_html(index=False)

        #Visualization
        plt.figure(figsize=(8, 6))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
        plt.tight_layout()
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        graph_url = base64.b64encode(img.getvalue()).decode('utf-8')

        #Pass all these to the template
        return render(request, 'result.html', {
            'first_few_rows': first_few_rows,
            'summary_statistics': summary_statistics,
            'missing_values': missing_values_html,
            'graph_url': graph_url
        })

    return render(request, 'upload.html')
