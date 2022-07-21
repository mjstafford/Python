console.log("connection test")

//some sites require API key
//Also may require header or other information
const API_KEY = "the_real_api_key_here"

async function handleNewsRequest(event) {
    event.preventDefault();

    const searchTerm = document.querySelector("#searchTerm").value
    const pageSize = document.querySelector("#pageSize").value
    const URL = `https://newsapi.org/v2/everything?q=${searchTerm}&pagesize=${pageSize}`
    console.log(URL)

    //news api requires a header
    const settings = {
        method: "GET",
        Headers: {
            "x-api-key": API_KEY
        }
    }

    const response = await fetch(URL, settings)
    const data = await response.json()
    console.log(data)

    const results = document.querySelector(".results")
    results.innerHTML = ""

    for (const article of data.articles) {
        results.innerHTML += `
            <div class="article">
                <h2>${article.title}</h2>
                <img src=${article.urlToImage} />
                <h5>${article.author}</h5>
                <p>${article.description}</p>
            </div>
        `
    }
}