function onSelectionChange(form) {
    let select = form.querySelector('select');
    return select.options[select.selectedIndex];
}

function onMultiSelectionChange(form) {

    options = form.querySelectorAll('option');
    let selectedList = [];
    options.forEach(opt => {
        if (opt.selected) {
            selectedList.push(opt.getAttribute('value'));
        }
    });

    return selectedList;
}