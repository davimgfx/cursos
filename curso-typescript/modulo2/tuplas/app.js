"use strict";
// Coleção Heterogênea de valores
let pessoa;
pessoa = ["Rogerinho", "Popye", 21, 1920];
console.log(pessoa[0]);
//TypeScript  com Spread Operator
// Lista HOMOGENEA
let listaFrutas;
listaFrutas = ["abacaxi", "abobora", "pera", "maça", "abacate"];
//console.log(...listaFrutas)
// Lista Heterogenea
let listaNovasFrutas = [listaFrutas.length, true, ...listaFrutas];
console.log(...listaNovasFrutas);
// Com label
let minhasInfos = ["Davi", 21];
const listarPessoas = (nomes, idades) => {
    return [...nomes, ...idades];
};
console.log(listarPessoas(["Davi", "gALUCE"], [31, 82]));
