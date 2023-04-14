const form = document.getElementById('search-form');
const input = document.getElementById('search-input');
const resultsContainer = document.getElementById('results-container');

const backendUrl = 'http://localhost:8000/search'; // Replace with your backend URL

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const query = input.value.trim();
    if (query) {
        try {
            const response = await fetch(`${backendUrl}?query=${encodeURIComponent(query)}&max_results=10`);
            const data = await response.json();
            displayResults(data);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }
});

function displayResults(data) {
    resultsContainer.innerHTML = '';
    if (data.length === 0) {
        resultsContainer.innerHTML = '<p>No results found.</p>';
        return;
    }
    let counter = 1;

    for (const paper of data) {
        const paperElement = document.createElement('div');
        paperElement.classList.add('paper');

        const title = document.createElement('p');
        title.classList.add('paper-title');
        title.textContent = `${counter}. ${paper.title}`;

        const authors = document.createElement('p');
        authors.classList.add('paper-authors');
        authors.textContent = `Authors: ${paper.authors.map(author => author.name).join(', ')}`;

        // const summary = document.createElement('p');
        // summary.classList.add("paper-summary");
        // summary.textContent = `Summary: ${paper.summary}`;

        const summary = document.createElement('p');
        summary.classList.add("paper-summary");

        // Create a span element for the "Summary:" keyword
        const summaryKeyword = document.createElement('span');
        summaryKeyword.classList.add("summary-keyword");
        summaryKeyword.textContent = 'Summary: ';

        // Create a span element for the actual summary text
        const summaryText = document.createElement('span');
        summaryText.classList.add("summary-text");
        summaryText.textContent = paper.summary;

        const link = document.createElement('a');
        link.classList.add('paper-link');
        link.href = paper.pdf_url;
        link.textContent = 'Read the paper';
        link.target = '_blank';

        paperElement.appendChild(title);
        paperElement.appendChild(authors);
        paperElement.appendChild(summary);
        summary.appendChild(summaryKeyword);
        summary.appendChild(summaryText);
        renderLatex(summaryText);
        paperElement.appendChild(link);
        resultsContainer.appendChild(paperElement);

        counter++;
    }
    
}

function renderLatex(element) {
    const regex = /\$([^\$]+)\$/g;
    const text = element.innerHTML;
    element.innerHTML = text.replace(regex, (match, latex) => {
        try {
            return katex.renderToString(latex);
        } catch (error) {
            console.error('Failed to render LaTeX:', error);
            return match;
        }
    });
}