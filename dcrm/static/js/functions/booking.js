function update_cost(){
    //Fetch through data again. It will not pull through correctly otherwise
    leave = document.getElementById("id_dateStart").value
    arrive = document.getElementById("id_dateEnd").value
    output = document.getElementById("output")
    error = document.getElementById("error")
    currentDate = new Date()
    //convert the data into dates and extract the difference in days
    leave = new Date(leave)
    arrive = new Date(arrive)
    console.log(leave)
    diff = arrive.getTime()-leave.getTime()
    days = Math.round(diff/(1000*60*60*24))

    //if correct times are chosen then calculate
    if(days>0 && adult>0 && child >0)
    {
        if(currentDate<arrive)   
        {
            output.innerHTML = (days*adult.value*50)+(days*child.value*50) 
            error.innerHTML = "";
        }
        else
        {
            error.innerHTML = "Please choose a starting date after the leaving date";
        }
    }
    if(adult<0 || child<0)
    {
        error.innerHTML = "Please put in positive numbers for children or adults";
    }
}


let adult = document.getElementById("id_adult");
adult.addEventListener("change",update_cost);
let child = document.getElementById("id_child");
child.addEventListener("change",update_cost);
let dateStart = document.getElementById("id_dateStart");
dateStart.addEventListener("change",update_cost);
let dateEnd = document.getElementById("id_dateEnd");
dateEnd.addEventListener("change",update_cost);