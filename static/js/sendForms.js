"use strict";

const d = document;


function submitPredefined(el) {
    let form = el.closest("form");

    let selectedEl = onSelectionChange(form);

    let data = { route: selectedEl.getAttribute("value") };
    let url = '/predefined';

    submit(url, data);
}

function submitCustom(el) {
    let form = el.closest("form");

    let selectedStr = onMultiSelectionChange(form).toString();

    let data = { route: selectedStr };
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
    console.log(data);

    fetch(url, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(data)
    })
        .then((response) => {
            console.log(response);
        });
}
