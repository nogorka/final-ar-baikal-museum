"use strict";

const d = document;


function submitPredefined(el) {
    let form = el.closest("form");

    let selectedEl = form.querySelector("option[selected]");

    let data = { route: selectedEl.getAttribute("value") };
    let url = '/predefined';

    submit(url, data);

}

function submitCustom(el) {
    let form = el.closest("form");

    let nodeList = form.querySelectorAll("option[value]");
    // let nodeList = form.querySelectorAll("option[selected]");
    //TODO - fix selected element

    let selectedEl = "";
    nodeList.forEach(element => {
        selectedEl += element.getAttribute('value') + ",";
    });

    let data = { route: selectedEl };
    let url = '/custom';

    submit(url, data);

}


function submitGenerated() {

    let data = { route: "" };
    let url = '/generated';

    submit(url, data);
}

function submit(url, data) {
    let headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    };

    fetch(url, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(data)
    })
        .then((response) => {
            console.log(response);
        });
}
