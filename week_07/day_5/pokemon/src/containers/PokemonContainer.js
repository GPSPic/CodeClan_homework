import { useEffect, useState } from "react";
import './PokemonContainer.css'
import PokemonDetails from "../components/PokemonDetails";
import PokemonList from "../components/PokemonList";

const PokemonContainer = () => {
    const [selectedPokemon, setSelectedPokemon] = useState(null)

    const [pokemons, setPokemons] = useState([])

    const getPokemons = () => {
        fetch('https://pokeapi.co/api/v2/pokemon?limit=20&offset=0')
            .then(res => res.json())
            .then(data => {
                const pokemonDetailsPromise = data.results.map(pokemon => {
                    return fetch(pokemon.url)
                        .then(res => res.json())
                })
            Promise.all(pokemonDetailsPromise)
                .then(pokemonDetails => setPokemons(pokemonDetails))
        })
    }

    useEffect(() => {
        getPokemons();
    }, []);

    const onSelectedPokemon = function(pokemon) {
        setSelectedPokemon(pokemon)
    }

    return ( 
        <>
            <h2>Choose your Starter:</h2>
            <div className="list-details">
                {pokemons ? 
                    <PokemonList pokemons={pokemons} onSelectedPokemon={onSelectedPokemon}/> : 
                    <p>Oh,oh! The database is down!</p>} 
                
                {selectedPokemon ? 
                    <PokemonDetails 
                    selectedPokemon={selectedPokemon}
                    name={selectedPokemon.name}
                    sprite={selectedPokemon.sprites.other['official-artwork'].front_default}
                    /> :
                    <p>Choose your favourite!</p>
                    }
            </div>
        </>
    );
}
 
export default PokemonContainer;

