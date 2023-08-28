// ! Não utilizar any!!! Apenas quando necessário
let oPerigo: any = "perigo"
oPerigo = 666
console.log(oPerigo)

let olhaOPerigo
olhaOPerigo = "perigo"
console.log(olhaOPerigo)

// * Quando usar (Recomendado o Unkown)
const formulario: {[campoFormulario: string] : any} = {
    nome: "Davi",
    idade: 24,
    taLogado: true
}
console.log(formulario)