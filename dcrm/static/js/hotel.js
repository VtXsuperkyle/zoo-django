function update_cost(){
    // inform the user of the cost of choice
    document.getElementById("booking_button").disabled = true;

    // get dates
    let arrive = document.getElementById('id_hotel_booking_date_arrive').value
   let leave = document.getElementById('id_hotel_booking_date_leave').value
   let price = document.getElementById('hotel_output')
   // calculate number of days
   arrive = new Date(arrive)
   leave = new Date(leave)
   diff = leave.getTime() - arrive.getTime();
   days = Math.round(diff/(1000*60*60*24));
   console.log("Days")
   // check the days is valid
   if (String(days) == "NaN"){

    price.innerHTML = "Hotel cost: Dates Not Chosen"
   
   }else{

    if (days > 0){
        if (adults.value + children.value + oaps.value > 0){
                // calculate costs
                let total = parseInt(adults.value) * 65
                + parseInt(children.value) * 35
                + parseInt(oaps.value) * 45

            //multiply by number of nights booked
            total = total * days


            //console.log("Total:" + String(total))

            // update the display for the user

            price.innerHTML = "Hotel cost: £" + String(total)
            document.getElementById("booking_button").disabled = false;

        }else{

            price.innerHTML = "A least 1 adult should be chosen"
        }
    }else{
        price.innerHTML = "Date not acceptable"
    }
   }
}

// get html elements
let adults = document.getElementById("id_hotel_booking_adults");
adults.addEventListener("change", update_cost)
let children = document.getElementById("id_hotel_booking_children");
children.addEventListener("change", update_cost)
let oaps = document.getElementById("id_hotel_booking_oap");
oaps.addEventListener("change", update_cost)

// TO DO: add the same updates for the date fields
let arrive_date = document.getElementById("id_hotel_booking_date_arrive");
arrive_date.addEventListener("change", update_cost)

let leave_date = document.getElementById("id_hotel_booking_date_leave");
leave_date.addEventListener("change", update_cost)