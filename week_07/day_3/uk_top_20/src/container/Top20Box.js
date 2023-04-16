import React, { useEffect, useState } from 'react';

import Top20List from "../components/Top20List";
import Header from "../components/Header"

const Top20Box = () => {

    const [top20, setTop20] = useState([]);

    useEffect(() => {
        getTop20();
    }, []);

    const getTop20 = function () {
        fetch('https://itunes.apple.com/gb/rss/topsongs/limit=20/json')
        .then(res => res.json())
        .then(data => setTop20(data.feed.entry))
    };



    return ( 
        <>
            <Header />
            <Top20List top20={top20}/>
        </>
     );
}
 
export default Top20Box;