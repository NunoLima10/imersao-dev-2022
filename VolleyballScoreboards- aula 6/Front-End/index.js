const hello_text = document.getElementById("Hello_text");


async function get_text(){
    const response =  await fetch("http://127.0.0.1:3000")
    const data = await response.json()
    hello_text.innerText = data.data
    
}

get_text()