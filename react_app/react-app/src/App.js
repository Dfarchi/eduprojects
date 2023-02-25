import './App.css';
import FlightCard from "./FlightCard";
import { flights } from './flights_data.js';



export default function FlightDisplay(props) {

    const flightItems = flights.map(
        (flight) => <FlightCard key={props.flight_num} flight={flight}/>)

    return (
    <>
      {flightItems}
    </>
    )
}

