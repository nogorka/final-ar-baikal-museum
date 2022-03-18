function onSelectionChange(select) {
    let prevSelected = select.querySelector("option[selected]");

    if (prevSelected != null) {
        prevSelected.removeAttribute("selected"); // remove old selected
    }

    var selectedOption = select.options[select.selectedIndex];
    selectedOption.setAttribute("selected", "");
} 

function onMultiSelectionChange(select) {

    console.log(select);
}