fetch('http://127.0.0.1:8000/fruit_app/')
    .then(response => response.json())
    .then(data => {
        const list = document.getElementById('fruits-list');
        list.innerHTML = '';
        data.forEach(fruit => {
            const li = document.createElement('li');
            li.innerHTML = `
                        <span class="fruit-name">${fruit.name}</span>
                        <span>${fruit.weight}</span>
                        <span class="fruit-color ${fruit.color}">${fruit.color}</span>
                    `;
            list.appendChild(li);
        });
    })
    .catch(() => {
        document.getElementById('fruits-list').innerHTML = '<li>Fehler beim Laden der Früchte.</li>';
    })