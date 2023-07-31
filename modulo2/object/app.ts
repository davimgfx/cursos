// Representa valores que não são primitivos
// Interface ou Type

// object x Object x {}
// Qualquer valor não primitivo x Funcionalidae x objeto sem propriedade próprio

const pessoaTest = {
    nome: "Davi",
    idade: 29,
    eHomem: true,
    comidasPreferidas: ["uva", "lasanha", "castanha"]
}

console.log(pessoaTest)

// Desetruturação do objeto
function onBoarding01(funcionario: { nome: string }){
    return funcionario.nome.toLowerCase()
}

console.log(onBoarding01(pessoaTest))

// Objetos nomeados