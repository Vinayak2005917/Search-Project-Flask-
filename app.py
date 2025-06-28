import flask
from flask import render_template, request, jsonify
from linear_search import linear_search, read_data_file
import os

app = flask.Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    try:
        data = request.get_json()
        query = data.get('query', '').strip()
        
        if not query:
            return jsonify({'error': 'No search query provided'}), 400
        
        # Read the data file
        data_file_path = os.path.join(os.path.dirname(__file__), 'data.txt')
        text_data = read_data_file(data_file_path)
        
        if not text_data:
            return jsonify({'error': 'Data file not found or empty'}), 500
        
        # Perform linear search
        results = linear_search(text_data, query)
        
        return jsonify({
            'query': query,
            'results_count': len(results),
            'results': results[:50]  # Limit to first 50 results for performance
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


