

export default function Time(props) {
    const dateDiff = Math.ceil((props.origTime - props.destTime)     / (1000 * 60 * 60 * 24))
    console.log(dateDiff)
return (<h4 id = 'time_left'> {dateDiff} </h4>)
}
