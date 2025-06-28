let currentFilter = 'Linear';

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    setupEventListeners();
});

function setupEventListeners() {
    // Search input enter key
    document.getElementById('searchInput').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            performSearch();
        }
    });

    // Filter buttons
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            currentFilter = this.dataset.filter;
            performSearch(); // Re-search when filter changes
        });
    });
}

function performSearch() {
    const query = document.getElementById('searchInput').value.trim();
    if (!query) {
        alert('Please enter a search term');
        return;
    }
    showLoading();
    // Use the currentFilter to select the algorithm
    let algorithm = currentFilter;
    // Normalize filter names if needed
    if (algorithm === 'all') algorithm = 'Linear';
    if (algorithm === 'Horspool ') algorithm = 'Horspool';
    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: query, algorithm: algorithm })
    })
    .then(response => response.json())
    .then(data => {
        hideLoading();
        if (data.error) {
            console.error('Search error:', data.error);
            showNoResults();
        } else {
            displayResults(data);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        hideLoading();
        showNoResults();
    });
}
function showLoading() {
    document.getElementById('loadingIndicator').style.display = 'block';
    document.getElementById('resultsContainer').style.display = 'none';
    document.getElementById('noResults').style.display = 'none';
}

function hideLoading() {
    document.getElementById('loadingIndicator').style.display = 'none';
}

function displayResults(data) {
    const resultsContainer = document.getElementById('resultsContainer');
    const resultsList = document.getElementById('resultsList');
    const resultsCount = document.getElementById('resultsCount');
    const noResults = document.getElementById('noResults');
    
    // Hide no results message
    noResults.style.display = 'none';
    
    // Update results count
    resultsCount.textContent = `${data.results_count} results found for "${data.query}"`;
    
    // Clear previous results
    resultsList.innerHTML = '';
    
    if (data.results_count > 0) {
        // Show results container
        resultsContainer.style.display = 'block';
        
        // Create result items
        data.results.forEach(result => {
            const resultItem = createResultItem(result, data.query);
            resultsList.appendChild(resultItem);
        });
    } else {
        showNoResults();
    }
}

function createResultItem(result, query) {
    const div = document.createElement('div');
    div.className = 'result-item';
    
    // Highlight the search term in the content
    const highlightedContent = highlightSearchTerm(result.content, query);
    
    div.innerHTML = `
        <div class="result-header">
            <div class="result-title">Line ${result.line_number}</div>
            <div class="result-meta">Position: ${result.position}</div>
        </div>
        <div class="result-content">${highlightedContent}</div>
    `;
    
    return div;
}

function highlightSearchTerm(text, searchTerm) {
    if (!searchTerm || !text) return text;
    
    const regex = new RegExp(`(${escapeRegex(searchTerm)})`, 'gi');
    return text.replace(regex, '<mark>$1</mark>');
}

function escapeRegex(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function showNoResults() {
    document.getElementById('resultsContainer').style.display = 'none';
    document.getElementById('noResults').style.display = 'block';
}
