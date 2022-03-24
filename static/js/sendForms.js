"use strict";

function submitPredefined(el) {
    let form = el.closest("form");
    let selectedEl = onSelectionChange(form);

    let data = {
        route: selectedEl.getAttribute("value"),
        type: "predefined"
    };

    submit(data);
}

function submitCustom(el) {
    let form = el.closest("form");
    let selectedStr = onMultiSelectionChange(form).toString();

    let data = {
        route: selectedStr,
        type: "custom"
    };

    submit(data);
}


function submitGenerated() {

    let data = {
        route: "",
        type: "generated"
    };

    submit(data);
}

function pushToLocalStorage(key, value) {
    localStorage.setItem(key, JSON.stringify(value));
}
function getFromLocalStorage(key) {
    JSON.parse(localStorage.getItem(key));
}

function submit(data) {

    let url = "/build_route";
    let headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    };


    fetch(url, {
        method: "POST",
        headers: headers,
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(route => {
            pushToLocalStorage("route", route.route);
            window.location.href = "/"; // redirect to start guide point
        })
}
