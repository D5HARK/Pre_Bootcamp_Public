function increase_like(){
   var initial_like_value = document.querySelector(".like_counter");
   console.log(typeof test);
   var new_like_value = parseInt(initial_like_value.innerHTML) + 1;
   initial_like_value.innerHTML = new_like_value;
}