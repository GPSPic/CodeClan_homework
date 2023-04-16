const PokemonDetails = ({selectedPokemon, name, sprite}) => {

    const capitalisePokemonName = (name) => {
        return name.charAt(0).toUpperCase() + name.slice(1)
    }
    const capitalisedName = capitalisePokemonName(name)

    return ( 
        <section className="pokemon-details">
            <p>You selected {capitalisedName}!</p>
            <img src={sprite} alt={name} height='200' width='200' />
        </section>
     );
}
 
export default PokemonDetails;