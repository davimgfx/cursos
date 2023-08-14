// for (let i = 0; i < 10; i++){
//     console.log(i)
// }

const arrayDesordemNumbers : number[] = [1, 22, 3, 10, 5, 6]
const arrayOrdemNumbers: number[] = arrayDesordemNumbers.sort((a,b) => a - b)
for( let i = 0 ; i < arrayOrdemNumbers.length ; i++){
    console.log(arrayOrdemNumbers[i])
}