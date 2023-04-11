// import React, { useState } from 'react';

import Movie from "./Movie";

const MovieList = ({movies}) => {
    return (  
        <ul> 
            {movies.map(movie =>
                <Movie 
                    key={movie.id}
                    name={movie.name}
                    url={movie.url}
                />
            )}
        </ul>
    )
};
 
export default MovieList;