const Song = ({song, index}) => {
    return ( 
        <li>#{index + 1} on the charts, {song["im:name"].label} by {song["im:artist"].label}</li>
     );
}
 
export default Song;