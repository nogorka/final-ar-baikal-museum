"use strict";


function pushToLocalStorage(key, value) {
    localStorage.setItem(key, JSON.stringify(value));
}
function getFromLocalStorage(key) {
    return JSON.parse(localStorage.getItem(key));
}

function getCurRouteIndex() {
    return Number(localStorage.getItem("routeIndex"));
}

function getRouteEl(id) {
    let array = getFromLocalStorage("route");
    console.log(array, id, array[id]);
    return array[id]
}

function moveToTheNextLoc() {
    let curIndx = getCurRouteIndex();
    let routeDist = getFromLocalStorage('route').length - 1;

    if (curIndx < routeDist) {
        pushToLocalStorage("routeIndex", curIndx + 1);
        let url = "/route?depart=" + getRouteEl(curIndx) + "&dest=" + getRouteEl(curIndx + 1);
        window.location.href = url;
    } else {
        window.location.href = "/";
    }
}

function showCurEntity() {
    let curIndx = getCurRouteIndex()+1;
    window.location.href = "/show/" + curIndx;
}

let tracker = document.getElementById("face-anchor");

tracker.addEventListener("zappar-visible", () => {
    console.log("move to the next location");

    showCurEntity();

});

tracker.addEventListener("zappar-notvisible", () => {
    console.log("Face is no longer visible");
});


