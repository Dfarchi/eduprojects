

export default function Time(props) {
    // console.log(date)
    const diffTime = Math.abs(props.origTime - props.destTime);
    const dateDiff = Math.ceil((diffTime)/ (1000 * 60 * 60 * 24))
    if (props.type == '1')
    var ret_val = `${props.origTime}`
    else if (props.type == '2')
        var ret_val = `${props.destTime} + (${dateDiff})`

    return (
        <h3>
        {ret_val}
        </h3>
    )
    }
