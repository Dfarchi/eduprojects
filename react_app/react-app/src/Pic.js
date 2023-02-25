
export default function Pic(props) {
    return (
      <div>
        <img id="orig" src={props.origPic} alt="Origin" width="200" height="200" />
        <img id="dest" src={props.destPic} alt="Destination" width="200" height="200" />
      </div>
    );
  }
  