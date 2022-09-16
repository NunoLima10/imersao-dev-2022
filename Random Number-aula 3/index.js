var value_of_luck = Math.floor(Math.random() * 11)

function valid_number(){
    var value = document.getElementById("input").value;
    var status = document.getElementById("status")
    status.innerText =""
    var submit_button = document.getElementById("submit_button");
    submit_button.disabled = (value < 0 || value > 10);
}

function test_luck(){
    var status = document.getElementById("status");
    var value = document.getElementById("input").value;
    if (!value){return}
    if (value != value_of_luck){
        status.innerText = "You lost"
        return       
    }
    status.innerText = "You won"
        value_of_luck = Math.floor(Math.random() * 11)
}