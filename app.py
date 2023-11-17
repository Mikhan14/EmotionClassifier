from flask import Flask, render_template, request, jsonify
import pandas as pd
import plotly.express as px
import json
import os
import plotly
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            file_path = os.path.join(app.root_path, uploaded_file.filename)
            uploaded_file.save(file_path)
            df = pd.read_excel(file_path)

            # Perform your data analysis here
            total_rows = len(df)
            emotions_counts = df.iloc[:, 1:].sum()
            fig = px.bar(emotions_counts, x=emotions_counts.index, y=emotions_counts.values, labels={'index': 'Emotion', 'y': 'Count'})
            graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

            return jsonify({'total_rows': total_rows, 'emotions_counts': emotions_counts.to_dict(), 'graph_json': graph_json})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
