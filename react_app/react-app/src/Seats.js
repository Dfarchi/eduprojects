

export default function Seats({seats_left}){
    
   let num_color = ''
   console.log(seats_left)
    if (seats_left >= 20){
        num_color = 'green'
    } else if (seats_left >= 8 && seats_left <20 ) {
        num_color = 'yellow'
    }
    else if (seats_left >0 && seats_left <8){
        num_color = 'red'
    }
    else {
        seats_left = "No seats left"
    }

    return (<h5 id = "seats_card" style={{color: num_color}}> {seats_left}</h5> )
     
     }
    
    