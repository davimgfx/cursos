// Uso de colchetes
let frutas: string[] = ["abacaxi", "abobora", "pera", "maça", "abacate"];
let quantidadeDeFrutas: number = frutas.length;
let soFrutaQueComecaComAb = frutas.filter((fruta) => fruta.startsWith("ab"));
// let percorrendoOArrayDeFrutas = frutas.map((fruta) => console.log(fruta))

frutas.push("banana")
// console.log(quantidadeDeFrutas, soFrutaQueComecaComAb);

// Com função
function imprimirFrutas(arrayDeFrutas: string[]){
    return arrayDeFrutas.map((fruta) => console.log(fruta))
}

imprimirFrutas(frutas)

// Array Objeto
let novasFrutas: Array<string> = ["abacaxi", "abobora", "melão"]

let contarNumeros: Array<number> = [1, 2, 3, 4, 5, 6]
contarNumeros = [...contarNumeros, 7, 8, 9 , 10]

// console.log(novasFrutas, contarNumeros)
