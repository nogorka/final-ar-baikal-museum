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
    return array[id]
}

function moveToTheNextLoc() {
    let curIndx = getCurRouteIndex();
    let prevIndx = curIndx - 1;
    let routeDist = getFromLocalStorage("route").length;

    if (curIndx < routeDist) {
        let url = "/route?depart=" + getRouteEl(prevIndx) + "&dest=" + getRouteEl(curIndx);
        pushToLocalStorage("type", "route");

        window.location.href = url;
    } else {
        window.location.href = "/";
    }
}

function showCurEntity() {
    let curIndx = getCurRouteIndex();
    let curEntity = getFromLocalStorage("route")[curIndx];

    pushToLocalStorage("type", "show");
    pushToLocalStorage("routeIndex", curIndx + 1);

    if (curEntity == 0) {
        window.location.href = "/";
    }
    else {
        window.location.href = "/show/" + curEntity;
    }
}
