-//Enuamerar os valores, mapeiam chaves para valores
//Estruturas de dados não ordenadas
/* 

Enum TypeName{
    constant1,
    constant2,
    constant3,
}


Por que usar ?
- Facilidade em mudar valores
- Reduz erro
- Funciona somente em tempo de compilação
- O tempo de execução será mais preciso e rapido
- Permite criar constante
*/

// Numeric Enums
enum Idiomas{
    Portugues,
    Frances,
    Espanhol,
    Ingles
}

console.log(Idiomas)
console.log(Idiomas.Portugues)
// Não é recomendado tipo string

//String Enums 

enum Dias {
    segunda = "seg",
    terca = "ter",
    quarta = "qua",
    quinta = "qui",
    sexta = "sex",
    sabado = "sab",
    domingo = "dom"
}

console.log(Dias)
console.log(Dias["segunda"])

const enum Comidas {
    Pizza = "Pizza",
    CachorroQuente = "Dog",
    Misto = "Misto"
}

function comida(c: Comidas) {
    return `Comida muito boa ${c}`
}

console.log(comida(Comidas.Misto))