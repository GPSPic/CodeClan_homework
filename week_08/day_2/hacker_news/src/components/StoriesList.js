const StoriesList = ({stories}) => {

    const storiesElement = stories.map((story) => {
        return <li key={story.id}><a href={story.url}>{story.title}</a></li>
    })

    return ( 
        <>
            {stories.length === 1 ? <h2>There is 1 story available</h2> : <h2>There are {stories.length} stories available.</h2>     }
            <ul>
                {storiesElement}
            </ul>
        </>
     );
}
 
export default StoriesList;