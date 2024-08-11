function showInput() { // this might be of no need
    var checkboxes = document.getElementsByTagName("input");
    var checkboxesChecked = [];
    for (var i = 0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked) {
            checkboxesChecked.push(checkboxes[i].defaultValue);
            // checkboxesChecked[i] = checkboxes[i].defaultValue;
        }
    }
    console.log(checkboxesChecked)
    if (checkboxesChecked.length < 5){
        alert("All field is required")
        return false
    }
    return true
}

function selectOnlyThis(id, name) {
    console.log('clicked')
    var myCheckbox = document.getElementsByName(name);
    
    for(var i=1; i<=myCheckbox.length; i++){
    if(document.getElementById(name+'_check'+i).value !=null){
        document.getElementById(name+"_check"+i).checked = false;
    }
    document.getElementById(id).checked = true
    }
}