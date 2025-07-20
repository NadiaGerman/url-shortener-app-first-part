document.getElementById('shorten-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const longUrl = document.getElementById('long-url').value;
    const lambdaUrl = 'https://qlm6jwvbp7wrmdtscfkjv3dxfa0pxwst.lambda-url.us-west-2.on.aws/shorten';
    try {
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
            document.getElementById('result').textContent =
                'Error: ' + (data.message || 'Unknown error');
        }
    } catch (err) {
        document.getElementById('result').textContent =
            'Error: ' + err.message;
    }
});
