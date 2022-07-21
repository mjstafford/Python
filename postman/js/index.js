console.log("connection test")

async function handleDogFormRequest(event) {
    //default action for submitting the form is to reload the page
    // we want to just update a portion of the page so we want to stop that from happening
    event.preventDefault();

    //gets the element .... and then gets the value from that
    const numberOfDogs = document.querySelector("#numberOfDogs").value
    console.log(numberOfDogs)

    //settings handles the authorization token, headers, etc...
    const settings = {
        method: "GET"
    }

    const URL = `https://dog.ceo/api/breeds/image/random/${numberOfDogs}`
    console.log(URL)

    const response = await fetch(URL, settings)
    const data = await response.json()
    console.log(data)

    const resultDiv = document.querySelector(".results")
    //Resets the resultDiv on each search
    resultDiv.innerHTML = "";

    //message is a key in the data coming from the api
    for (const image of data.message) {
        resultDiv.innerHTML += `
            <div class="dogImageContainer">
                <img src="${image}" alt="Dog Image" class="dogImage"/>
            </div>
        `;
    }
}


//alternative method
// function handleDogFormRequest(event) {
//     //default action for submitting the form is to reload the page
//     // we want to just update a portion of the page so we want to stop that from happening
//     event.preventDefault();

//     //gets the element .... and then gets the value from that
//     const numberOfDogs = document.querySelector("#numberOfDogs").value
//     console.log(numberOfDogs)

//     //settings handles the authorization token, headers, etc...
//     const settings = {
//         method: "GET"
//         // EXAMPLE of more complicated settings
//         // ,headers: {
//         //     "Authorization": Token,
//         //     body: JSON.stringify(data)
//         // }
//     }

//     const URL = `https://dog.ceo/api/breeds/image/random/${numberOfDogs}`
//     console.log(URL)

//     fetch(URL, settings)
//         //using anonymous function in this example
//         .then(function (response) {
//             console.log(response)
//         })
//         .then()
//         .then()
// }

