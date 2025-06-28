import flask
from flask import render_template, request, jsonify
from linear_search import linear_search, read_data_file as read_linear_data_file
from Hoospool import horspool_search, read_data_file as read_horspool_data_file
from Boyer_Moore import boyer_moore_search, read_data_file as read_boyer_data_file
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
        
        # Determine which algorithm to use
        algorithm = data.get('algorithm', 'Linear').strip()
        # Normalize algorithm name for robustness
        normalized_algorithm = algorithm.replace('-', '_').replace(' ', '').lower()
        data_file_path = os.path.join(os.path.dirname(__file__), 'data.txt')

        if normalized_algorithm == 'linear':
            text_data = read_linear_data_file(data_file_path)
            if not text_data:
                return jsonify({'error': 'Data file not found or empty'}), 500
            results = linear_search(text_data, query)
        elif normalized_algorithm == 'horspool':
            text_data = read_horspool_data_file(data_file_path)
            if not text_data:
                return jsonify({'error': 'Data file not found or empty'}), 500
            results = horspool_search(text_data, query)
        elif normalized_algorithm == 'boyer_moore':
            text_data = read_boyer_data_file(data_file_path)
            if not text_data:
                return jsonify({'error': 'Data file not found or empty'}), 500
            results = boyer_moore_search(text_data, query)
        else:
            return jsonify({'error': f'Unknown algorithm: {algorithm}'}), 400

        return jsonify({
            'query': query,
            'results_count': len(results),
            'results': results[:50]  # Limit to first 50 results for performance
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


