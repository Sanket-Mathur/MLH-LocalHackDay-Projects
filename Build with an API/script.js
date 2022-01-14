var news = [];

function displayNews() {
    var page = document.getElementById('container');

    news.forEach(element => {
        let heading = document.createElement('h2');
        heading.innerHTML = element.title;
        page.appendChild(heading);

        let description = document.createElement('p');
        description.innerHTML = element.description;
        page.appendChild(description);

        let url = document.createElement('a');
        url.target = '_blank';
        url.href = element.url;
        url.innerHTML = element.url;
        page.appendChild(url);

        page.appendChild(document.createElement('hr'));
    });
}

async function fetchNews() {
    news = await fetch('https://saurav.tech/NewsAPI/top-headlines/category/technology/in.json')
        .then(response => response.json())
        .then(data => data.articles)
        .then()
        .catch(error => console.log(error));
    
    displayNews();
}

fetchNews();