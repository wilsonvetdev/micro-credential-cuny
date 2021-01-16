function showLarge(thisGraphic) {
    thisGraphic.style.width = '170px';
    thisGraphic.style.height = '170px';
    thisGraphic.style.marginRight = '10px';
    thisGraphic.style.marginTop = '20px';
}


function showNormal(thisGraphic) {
    thisGraphic.style.width = '140px';
    thisGraphic.style.height = '140px';
    thisGraphic.style.marginRight = '40px';
    thisGraphic.style.marginTop = '50px';
}

let italianImages = document.querySelectorAll('.italianImages')

console.log(italianImages.length)

italianImages.forEach(image => {
    image.addEventListener("mouseenter", () => {
        showLarge(image)
    })

    image.addEventListener("mouseleave", () => {
        showNormal(image)
    })
})