
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

// Using optional no object

interface Pessoa04 {
    nome: string;
    idade: number;
    isAdmin: boolean;
    email ?: string;
}

function onboarding4(pessoa: Pessoa04) {
    console.log("Seja bem vinda " + pessoa.nome + " com a idade " + pessoa.idade)
}

onboarding4({ nome: "Glaucia Lemos", idade: 22, isAdmin: false }) 

// Interface

interface Pessoa05{
    nome: string;
    funcao: string;
    readonly email: string; 
}

function onboarding5(pessoa: Pessoa05) {
    console.log("Seja bem vinda " + pessoa.nome + " com a função " + pessoa.funcao + " email " + pessoa.email)
}

onboarding5({ nome: "Davi", funcao: "alegrin", email: "davi@gmail.com"})

// Heranças com objetos
interface Mae {
    nome: string
}

interface Pae {
   sobrenome: string
}

interface Filha extends Pae, Mae{
    idade: number
}

const filha: Filha = {
    nome: "Meu nome",
    sobrenome: "Meu sobrenome",
    idade: 35
}

console.log(filha)

// Interseções

interface Email {
    email: string
}

type EmailApi = Email | null


// Generic objects

type Usuario = {
    nome: string;
    email: string;
}

type Admin = {
    nome: string;
    email: string;
    admin: boolean
}

const usuario: Usuario = {
    nome: "Davi",
    email: "davi@gmail.com"
}


const admin: Admin = {
    nome: "Davi",
    email: "davi@gmail.com",
    admin: true,
}

// Este T, signfica que a função é generica e aceita varios tipos diferentes

function acessarSistema<T>(usuario: T): T{
    return usuario
}

console.log(acessarSistema<Usuario>(usuario))
console.log(acessarSistema<Admin>(admin))

