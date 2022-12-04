const contentContainer = document.getElementById('content-container')
const loginForm = document.getElementById("login-form")
const baseendpoint = "http://localhost:8000"

if(loginForm){
    loginForm.addEventListener("submit", handlelogin)
}

function handlelogin(event){
    event.preventDefault()
    const loginendpoint = `${baseendpoint}/api/token/`
    let loginformdata = new FormData(loginForm)
    let loginobjectdata = Object.fromEntries(loginformdata)
    let bodystr = JSON.stringify(loginobjectdata)
    const options = {
        method : "POST",
        headers :{
            "content-type": "application/json"
        },
        body : bodystr
    }
    fetch(loginendpoint, options)
    .then(response =>{
        return response.json()
    })
    .then( authdata => {
        handleAuthData(authdata, getProductList)
    })
    .catch(err =>{
        console.log('err', err)
    })
}

function writeToContainer(data){
    if (contentContainer){
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "</pre>"
    }
}

function handleAuthData(authdata, callback) {
    localStorage.setItem("access", authdata.access)
    localStorage.setItem("refresh", authdata.refresh)
    if(callback) {
        callback()
    }
}

function getProductList(){
    const endpoint = `${baseendpoint}/products/`
    options = {
        method : "GET",
        headers : {
            "content-type": "application/json",
            "Authorization" :`Token ${localStorage.getItem('access')}`
        }
    }
    fetch(endpoint, options)
    .then(response => {
        console.log(response)
        return response.json()
    })
    .then(data=> {
        console.log(data)
        writeToContainer(data)
    })

}
