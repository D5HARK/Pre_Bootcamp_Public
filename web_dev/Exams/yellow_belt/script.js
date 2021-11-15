function remove_definition(element){
    element.remove();
}

function increase_like_one(){
    var initial_like_value = document.querySelector("#like_counter_one");
    var new_like_value = parseInt(initial_like_value.innerHTML) + 1;
    initial_like_value.innerHTML = new_like_value;
}
function increase_like_two(){
    var initial_like_value = document.querySelector("#like_counter_two");
    var new_like_value = parseInt(initial_like_value.innerHTML) + 1;
    initial_like_value.innerHTML = new_like_value;
}
function increase_like_three(){
    var initial_like_value = document.querySelector("#like_counter_three");
    var new_like_value = parseInt(initial_like_value.innerHTML) + 1;
    initial_like_value.innerHTML = new_like_value;
}

function search(){
    var input_entered = document.getElementById("search_bar").value;
    console.log(input_entered)
    var alert_text = "You are searching for " + input_entered + "!"
    alert(alert_text)
}