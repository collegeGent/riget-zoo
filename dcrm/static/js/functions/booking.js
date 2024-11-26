function update_cost(){
    console.log(adult.value)
}


let adult = document.getElementById("adult");
adult.addEventListener("change",update_cost);
let child = document.getElementById("child");
child.addEventListener("change",update_cost);
let dateStart = document.getElementById("dateStart");
dateStart.addEventListener("change",update_cost);
let dateEnd = document.getElementById("dateEnd");
dateEnd.addEventListener("change",update_cost);