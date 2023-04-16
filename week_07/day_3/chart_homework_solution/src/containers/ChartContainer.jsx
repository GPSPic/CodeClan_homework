import React, { useEffect, useState } from 'react';
import Chart from '../components/Chart';
import TitleBar from '../components/TitleBar';

const ChartContainer = ({ genres }) => {
  const [songs, setSongs] = useState([]);

  useEffect(() => {
    loadSongs(genres[0].url)
  }, [])
  //There was genre in the line 10 square brackets, was not needed it seems since genres is a set array and not a state

  const loadSongs = url => {
    fetch(url)
      .then(res => res.json())
      .then(songsList => setSongs(songsList.feed.entry))
      .catch(err => console.error(`Loading songs error: ${err}`));
  }

  const handleSelectChange = event => {
    loadSongs(event.target.value);
  }

  return (
    <>
      <TitleBar
        handleSelectChange={handleSelectChange}
        genres={genres}
      />
      <Chart
        songs={songs}
        url={genres[0].url}
        handleSelectChange={handleSelectChange}
      />
    </>
  )
}

export default ChartContainer;
