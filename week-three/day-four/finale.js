let body = document.querySelector('body')
let verticalButton = document.querySelector('button#vertical')
let horizontalButton = document.querySelector('button#horizontal')
let corgi = document.createElement('img')
corgi.src = 'Images/corgi.jpg'
let lab = document.createElement('img')
lab.src = 'Images/lab.jpg'
let terrier = document.createElement('img')
terrier.src = 'Images/terrier.jpg'
let position = 1
let begin

verticalButton.addEventListener('click', () => {
    if(begin) {
        clearInterval(begin)
    }
    begin = setInterval('renderVerticalImgs()', 500)
})

const corgiTop = () => {
    corgi.style.position = 'absolute'
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
    if(position === 1 ) {
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