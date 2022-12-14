fetch("https://api.frankfurter.app/currencies")
.then((data) => data.json())
.then((data) => {
    currencies_labels(data);
  });
function currencies_labels(data){
    const select_l = document.getElementById("select_l");
    const select_r = document.getElementById("select_r");
    const entries = Object.entries(data);
    console.log(entries)
    for(var i = 0 ; entries.length > i; i++){
      select_l.innerHTML += `<option value=${entries[i][0]}>${entries[i][1]}</option>` 
      select_r.innerHTML += `<option value=${entries[i][0]}>${entries[i][1]}</option>` 
    }
}
function converter(currency,to_currency,value){
  const host = "api.frankfurter.app"
  fetch(`https://${host}/latest?amount=${value}&from=${currency}&to=${to_currency}`)
  .then(res => res.json())
  .then(data =>{
    var input_readonly = document.getElementById("input_readonly")
    input_readonly.value = data.rates[to_currency]
  } )

}

function currency_convertor(){
  var status = document.getElementById("status")
  var input_currency = document.getElementById("input_currency").value
  var select_currency = document.getElementById("select_l").value
  var select_to_currency = document.getElementById("select_r").value

  if (input_currency== ''){
    status.innerHTML = "Invalid value"
    return
  }
  if (input_currency < 0){
    status.innerHTML = "Negative balance"
    return
  }

  if (select_currency == select_to_currency){
    status.innerHTML = "Select two different currencies"
    return
  }

  converter(select_currency, select_to_currency, input_currency)
  
  }


