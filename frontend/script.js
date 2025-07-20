document.getElementById('shorten-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const longUrl = document.getElementById('long-url').value;
    // Placeholder: Replace with your Lambda Function URL
    const lambdaUrl = 'https://<your-lambda-function-url>/shorten';
    const res = await fetch(lambdaUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: longUrl })
    });
    const data = await res.json();
    if (res.ok) {
        document.getElementById('result').innerHTML =
            `Short URL: <a href="${data.short_url}" target="_blank">${data.short_url}</a>`;
    } else {
        document.getElementById('result').textContent = 'Error: ' + (data.message || 'Unknown error');
    }
});
