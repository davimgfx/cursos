// Não sabe qual tipo definir
// Any !== unknown
// O unknown verifica o tipo, enquanto o any não
// Ordem unknown -> any

let valorDaVariavel: unknown

valorDaVariavel = true

valorDaVariavel = 123

valorDaVariavel = "string"

valorDaVariavel = ["Davi", 21]

// ! Error

// let valorDaVariavel: boolean

console.log(valorDaVariavel)