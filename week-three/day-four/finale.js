let body = document.querySelector('body')

let verticalButton = document.querySelector('button#vertical')
let horizontalButton = document.querySelector('button#horizontal')
let diagonalButton = document.querySelector('button#diagonal')

let position = 1
let begin

verticalButton.addEventListener('click', () => {

    let corgi = document.createElement('img')
    corgi.src = 'Images/corgi.jpg'

    const corgiTop = () => {
        corgi.style.position = 'absolute'
        corgi.style.top = '0'
        corgi.style.left = '0'
        corgi.style.right = '0'
        corgi.style.margin = '0 auto auto auto'
        corgi.style.width = '320px'
        body.append(corgi)
    }

    const corgiCenter = () => {
        corgi.style.position = 'absolute'
        corgi.style.left = '0'
        corgi.style.right = '0'
        corgi.style.top = '0'
        corgi.style.bottom = '0'
        corgi.style.margin = 'auto'
        corgi.style.width = '320px'
        body.append(corgi)
    }

    const corgiBottom = () => {
        corgi.style.position = 'absolute'
        corgi.style.left = '0'
        corgi.style.right = '0'
        corgi.style.bottom = '0'
        corgi.style.margin = 'auto'
        corgi.style.marginBottom = '0'
        corgi.style.width = '320px'
        body.append(corgi)
    }

    const renderVerticalImgs = () => {
        if (position === 1) {
            corgiTop()
            position = 2
        } else if (position === 2) {
            corgiCenter()
            position = 3
        } else if (position === 3) {
            corgiBottom()
            position = 1
        }
    }

    if (begin && document.images.length > 0) {
        clearInterval(begin)
        for(let i = 0; i < document.images.length; i++) {
            document.images[i].remove()
        }
        position = 1
    } else {
        begin = setInterval(renderVerticalImgs, 500)
    }

})

horizontalButton.addEventListener('click', () => {

    let lab = document.createElement('img')
    lab.src = 'Images/lab.jpg'

    const labLeft = () => {
        lab.style.position = 'absolute'
        lab.style.left = '0'
        lab.style.top = '0'
        lab.style.bottom = '0'
        lab.style.margin = 'auto auto auto 0'
        lab.style.width = '320px'
        body.append(lab)
    }

    const labCenter = () => {
        lab.style.position = 'absolute'
        lab.style.left = '0'
        lab.style.right = '0'
        lab.style.top = '0'
        lab.style.bottom = '0'
        lab.style.margin = 'auto'
        lab.style.width = '320px'
        body.append(lab)
    }

    const labRight = () => {
        lab.style.position = 'absolute'
        lab.style.left = '0'
        lab.style.top = '0'
        lab.style.bottom = '0'
        lab.style.margin = 'auto 0 auto auto'
        lab.style.width = '320px'
        body.append(lab)
    }

    const renderHorizontalImgs = () => {
        if (position === 1) {
            labLeft()
            position = 2
        } else if (position === 2) {
            labCenter()
            position = 3
        } else if (position === 3) {
            labRight()
            position = 1
        }
    }

    if (begin && document.images.length > 0) {
        clearInterval(begin)
        for(let i = 0; i < document.images.length; i++) {
            document.images[i].remove()
        }
        position = 1
    } else {
        begin = setInterval(renderHorizontalImgs, 500)
    }

})

diagonalButton.addEventListener('click', () => {

    let terrier = document.createElement('img')
    terrier.src = 'Images/terrier.jpg'

    const terrierBottomLeft = () => {
        terrier.style.position = 'absolute'
        terrier.style.left = '0'
        terrier.style.bottom = '0'
        terrier.style.margin = 'auto auto 0 0'
        terrier.style.width = '320px'
        body.append(terrier)
    }

    const terrierCenter = () => {
        terrier.style.position = 'absolute'
        terrier.style.left = '0'
        terrier.style.right = '0'
        terrier.style.top = '0'
        terrier.style.bottom = '0'
        terrier.style.margin = 'auto'
        terrier.style.width = '320px'
        body.append(terrier)
    }

    const terrierTopRight = () => {
        terrier.style.position = 'absolute'
        terrier.style.right = '0'
        terrier.style.top = '0'
        terrier.style.margin = '0 0 auto auto'
        terrier.style.width = '320px'
        body.append(terrier)
    }

    const renderDiagonalImgs = () => {
        if (position === 1) {
            terrierBottomLeft()
            position = 2
        } else if (position === 2) {
            terrierCenter()
            position = 3
        } else if (position === 3) {
            terrierTopRight()
            position = 1
        }
    }
    
    if (begin && document.images.length > 0) {
        clearInterval(begin)
        for(let i = 0; i < document.images.length; i++) {
            document.images[i].remove()
        } 
        position = 1
    } else {
        begin = setInterval(renderDiagonalImgs, 500)
    }

})