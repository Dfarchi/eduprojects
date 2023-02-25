
export default function Pic(props) {
    const pic = Object.values(props)
    return (
      <div>
        <img id="orig" src={pic} alt="Origin" width="200" height="200" fit = "scale-down"/>
      </div>
    );
  }
  