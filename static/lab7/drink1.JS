function getPrice(params) {
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;

    const obj = {
        "method": "get-price",
        "params":{
            drink: drink,
            milk: milk,
            sugar: sugar
        }
    }

    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(obj)
    })
    .then(function(resp){
        return resp.json();
    })
    .then(function(data){
        document.querySelector('#price').innerHTML = `Цена напитка: ${data.result} руб.`;
        document.querySelector('#pay').style.display = '';
    })
}


function pay() {
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;
    const cardNumber = document.querySelector('[name=card]').value;
    const holderName = document.querySelector('[name=name]').value;
    const cvv = document.querySelector('[name=cvv]').value;

    const obj = {
        "method": "pay",
        "params":{
            drink: drink,
            milk: milk,
            sugar: sugar,
            card: cardNumber,
            name: holderName,
            cvv: cvv
        }
    }

    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(obj)
    })
    .then(function(resp){
        return resp.json();
    })
    .then(function(data){
        if(data.success){
            alert(`Оплата прошла успешно. С карты списано ${data.result} руб.`);
            document.querySelector('#cancel').style.display = '';
        } else {
            alert(`Ошибка при оплате: ${data.error}`);
            document.querySelector('#cancel').style.display = 'none';
        }
    })
}

function refund() {
    const cardNumber = document.querySelector('[name=card]').value;
    const holderName = document.querySelector('[name=name]').value;
    const cvv = document.querySelector('[name=cvv]').value;

    const obj = {
        "method": "refund",
        "params": {
            card: cardNumber,
            name: holderName,
            cvv: cvv
        }
    }

    fetch('/lab7/api', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(obj)
    })
    .then(function (resp) {
        return resp.json();
    })
    .then(function (data) {
        alert(data.message = `Сумма ${data.result} руб. вернулась на карту`); 
    })
}