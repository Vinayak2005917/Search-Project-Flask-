# Search Project

A mini project showcasing a series of string search algorithms (Linear Search, Horspool, and Boyer-Moore) using Python Flask for the backend and a modern JavaScript frontend.

## Features

- **Search Algorithms:** Choose between Linear Search, Horspool, and Boyer-Moore.
- **Fast Search:** Results are displayed instantly with a timer showing how long the search took.
- **Case-insensitive:** Searches are not case-sensitive.
- **Highlighting:** Search terms are highlighted in the results.
- **Responsive UI:** Clean, modern interface with filter buttons for algorithm selection.

## Project Structure

```
Search Project/
│
├── app.py                  # Flask backend
├── data.txt                # Data file to search
├── linear_search.py        # Linear search implementation
├── Hoospool.py             # Horspool search implementation
├── Boyer_Moore.py          # Boyer-Moore search implementation
│
├── templates/
│   └── index.html          # Main HTML template
│
└── static/
    ├── style.css           # CSS styles
    └── script.js           # Frontend JavaScript
```

## Getting Started

### 1. Install dependencies

Make sure you have Python 3.x installed.

```bash
pip install flask
```

### 2. Run the app

```bash
python app.py
```

The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### 3. Use the app

- Enter a search term in the input box.
- Select an algorithm using the filter buttons.
- View results, including the time taken for the search.

## Customization

- **Add more algorithms:** Implement a new Python file and connect it in `app.py` and the frontend.
- **Change UI:** Edit `templates/index.html` and `static/style.css`.

## License

This project is for educational purposes.
