const pessoaNaEmpresa = {
    nome: "Davi",
    sobrenome: "Costa",
    idade: 123
}


function onboarding(funcionario: { nome: string;}){
    console.log(funcionario.nome);
}

onboarding(pessoaNaEmpresa)

// Interface
interface Pessoa {
    nome: string;
    funcao: string; 
}

function onboarding2(pessoa: Pessoa) {
    console.log("Seja bem vinda " + pessoa.nome + " com a função " + pessoa.funcao)
}

onboarding2({ nome: "Glaucia Lemos", funcao: "Rei do pvp"})

//Type
type Pessoa03 = {
    nome: string;
    funcao: string; 
}

function onboarding3(pessoa: Pessoa03) {
    console.log("Seja bem vinda " + pessoa.nome + " com a função " + pessoa.funcao)
}

onboarding3({ nome: "Glaucia Lemos", funcao: "sinistra"})