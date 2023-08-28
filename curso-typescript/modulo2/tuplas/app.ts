// Coleção Heterogênea de valores
let pessoa: [string, string, number, number]
pessoa = [ "Rogerinho", "Popye", 21, 1920]
console.log(pessoa[0])

//TypeScript  com Spread Operator
// Lista HOMOGENEA
let listaFrutas: [string, ...string[]]
listaFrutas = ["abacaxi", "abobora", "pera", "maça", "abacate"]
//console.log(...listaFrutas)

// Lista Heterogenea
let listaNovasFrutas: [number, boolean, ...string[]] = 
[listaFrutas.length, true, ...listaFrutas]

console.log(...listaNovasFrutas)

// Com label
let minhasInfos: [nome: string, idade: number] = ["Davi", 21]

const listarPessoas = (nomes: string[], idades: number[]) => {
    return [...nomes, ...idades]
}

console.log(listarPessoas(["Davi", "gALUCE"], [31, 82]))