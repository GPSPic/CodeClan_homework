import Song from "./Song";

const Top20List = ({top20}) => {

    const songItems = top20.map((song, index) => {
        return <Song song={song} key={index} index={index}/>
    })

    return ( 
        <ul>
            {songItems}
        </ul>
     );
}
 
export default Top20List;