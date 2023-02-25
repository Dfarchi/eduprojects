import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import arrow from './flights_arrow.png';
import Pic from './Pic';
import Seats from './Seats';
import Time from './Time';

export default function Flight({ flight }) {
  const flightContainerStyle = {
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'center',
    border: '2px solid black'

  };

  const originContainerStyle = {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  };

  const destinationContainerStyle = {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  };

  const seatsContainerStyle = {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
  };

  return (
    <div style={flightContainerStyle}>
      <div style={originContainerStyle}>
        <Pic origPic={flight.origin.img_url} />
        <Time origTime={flight.origin.time} />
      </div>

      <div style={seatsContainerStyle}>
        <img src={arrow} alt="" />
        <Seats seats_left={flight.seats_left} />
      </div>

      <div style={destinationContainerStyle}>
        <Pic destPic={flight.destination.img_url} />
        <Time destTime={flight.destination.time} />
      </div>
    </div>
    
  );
}



// export default function FlightCard({flight}) {
//     const my_style = {
//         color: 'red',
//         backgroundColor: 'black'
//     }
//     my_style.fontSize = '20px'
//     return(
//         <div>
            
//             <div nsme = "origin">
//                 <Pic  origPic = {flight.origin.img_url}/>
//                 <Time origTime={flight.origin.time}/>
//             </div>
//                 <Seats seats_left={flight.seats_left}/>
//                 <img src={arrow} alt="" />

//             <div name = "destination">
//                 <Pic destPic={flight.destination.img_url}/>
//                 <Time destTime={flight.destination.time}/>
//             </div>
//         </div>
//     )

// }
