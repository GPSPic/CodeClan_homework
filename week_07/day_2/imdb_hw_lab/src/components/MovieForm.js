import React, { useState } from 'react';

const MovieForm = ({onMovieSubmit}) => {

    const [name, setName] = useState('')
    const [url, setUrl] = useState('')

    const handleNameChange = e => setName(e.target.value)
    const handleUrlChange = e => setUrl(e.target.value)

    const handleMovieSubmit = (event) => {
        event.preventDefault()
        const nameValue = name.trim()
        const urlValue = url.trim()

        onMovieSubmit({
            name: nameValue,
            url: urlValue,
        })

        setName('')
        setUrl('')
    }

    return ( 
        <form onSubmit={handleMovieSubmit}>
            <label htmlFor='name'>Add name: </label>
            <input type='text' 
                id='name' 
                placeholder='Enter name here' 
                required 
                value={name}
                onChange={handleNameChange}
                />
            <label htmlFor='url'>Add url: </label>
            <input type='text' 
                id='url' 
                placeholder='Enter link here' 
                required 
                value={url}
                onChange={handleUrlChange}
                />
            <button>Add an upcoming release</button>
        </form>
     );
}
 
export default MovieForm;