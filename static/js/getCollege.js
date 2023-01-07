const getCol = (arr){
    return arr.map(col => `<option value=${col}>${col}</option>`)
}
export default getCol;