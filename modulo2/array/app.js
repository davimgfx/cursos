"use strict";
// Uso de colchetes
let frutas = ["abacaxi", "abobora", "pera", "maça", "abacate"];
let quantidadeDeFrutas = frutas.length;
let soFrutaQueComecaComAb = frutas.filter((fruta) => fruta.startsWith("ab"));
// let percorrendoOArrayDeFrutas = frutas.map((fruta) => console.log(fruta))
frutas.push("banana");
// console.log(quantidadeDeFrutas, soFrutaQueComecaComAb);
// Com função
function imprimirFrutas(arrayDeFrutas) {
    return arrayDeFrutas.map((fruta) => console.log(fruta));
}
imprimirFrutas(frutas);
// Array Objeto
let novasFrutas = ["abacaxi", "abobora", "melão"];
let contarNumeros = [1, 2, 3, 4, 5, 6];
contarNumeros = [...contarNumeros, 7, 8, 9, 10];
// console.log(novasFrutas, contarNumeros)
