const dropList = document.querySelectorAll("form select"),
fromCurrency = document.querySelector(".from select"),
toCurrency = document.querySelector(".to select"),
getButton = document.querySelector("form button");
amountCurrency = document.getElementById("currencyValue");
startCurrency = document.getElementById("PLN-from");
endCurrency = document.getElementById("EUR-end");
resultExchangeRate = document.getElementById("result-exchange-rate");

let country_list = {
    "EUR" : "EU",
    "USD" : "US",
    "PLN" : "PL",
    "GBP" : "GB",
    "AUD" : "AU",
    "CHF" : "CH",
    "JPY" : "JP"
}

for (let i = 0; i < dropList.length; i++) {
    dropList[i].addEventListener("change", e =>{
        loadFlag(e.target);
    });
}

function start(){
    startCurrency.setAttribute("selected", "");
    endCurrency.setAttribute("selected", "");
}
start();

function loadFlag(element){
    for (let code in country_list){
        if (code == element.value){ // if currency code of country list is equal to option value
            let imgTag = element.parentElement.querySelector("img"); // selecting img tag of particular drop list
            // passing country code of a selected currency code in a img url
            imgTag.src = `https://flagcdn.com/48x36/${country_list[code].toLowerCase()}.png`;
        }
    }
}

getButton.addEventListener("click", e =>{
    e.preventDefault(); //preventing form from submitting
    getExchangeRate();
});

const exchangeIcon = document.querySelector("form .icon");
exchangeIcon.addEventListener("click", ()=>{
    let tempCode = fromCurrency.value; // temporary currency code of FROM drop list
    fromCurrency.value = toCurrency.value; // passing TO currency code to FROM currency code
    toCurrency.value = tempCode; // passing temporary currency code to TO currency code
    loadFlag(fromCurrency); // calling loadFlag with passing select element (fromCurrency) of FROM
    loadFlag(toCurrency); // calling loadFlag with passing select element (toCurrency) of TO
});
function getExchangeRate(){
    // console.log("Tu będzie wynik! ");
    // console.log(fromCurrency.value, toCurrency.value, amountCurrency.value);
    let xhr = new XMLHttpRequest();
    xhr.open("GET", "http://127.0.0.1:5000/calculation"+"?"+"amount="+amountCurrency.value+"&"+"from_curr="+fromCurrency.value+"&"+"to_curr="+toCurrency.value);
    xhr.setRequestHeader('Content-Type', 'application/json');
    // xhr.send(`{
    // "amount": amountCurrency.value, "from_curr": fromCurrency.value, "to_curr": toCurrency.value}`);
    xhr.onload = function () {
    if (xhr.readyState === xhr.DONE) {
        console.log(xhr.response);
        resultExchangeRate.innerText = amountCurrency.value+" "+fromCurrency.value.toString()+" = "+xhr.response+" "+toCurrency.value.toString();
    }

};

xhr.send(null);
    console.log(xhr.responseText);

}