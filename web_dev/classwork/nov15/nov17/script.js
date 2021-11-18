async function poke_me(query,e) {
    e.preventDefault();
    var response = await fetch(`https://pokeapi.co/api/v2/pokemon/${query}`)
    var coderData = await response.json()
    poke_name.innerHTML = `
    <p>${coderData.name}</p>`
    poke_image.innerHTML = `
    <img src="${coderData.sprites.front_default}">
    `
    console.log(coderData)
}
