const SearchField = ({onChangeUpdateSearchTerms}) => {

    const handleChange = function (e) {
        // console.log(e.target.value)
        onChangeUpdateSearchTerms(e.target.value)
    };

    return ( 
        <>
            <label htmlFor="search-input"></label>
            <input id="search-input" type="text" onChange={handleChange} placeholder="Search..."></input>
        </>
     );
}
 
export default SearchField;