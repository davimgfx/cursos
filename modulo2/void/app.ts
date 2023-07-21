// Função que retorna nenhum valor, mesma coisa de linguagens tipadas

// public static void classificacao(int lado1, int lado2, int lado3){
//     if(lado1 + lado2 > lado3 && lado1 + lado3 > lado2 && lado2 + lado3 > lado1){
//       if(lado1 == lado2 && lado2 == lado3){
//         System.out.println("É equilátero");
//       } else if (lado1 != lado2 && lado2 !=  lado3 && lado3 != lado2){
//         System.out.println("É isósceles");
//       } else {
//         System.out.println("É escaleno");
//       }
//     }
//     else{
//       System.out.println("Não é um triangulo");
//     }
// }

// Melhora a clareza do código

// Garante a segurança do tipo

// fuction exemploFuncao(mensagem): void {}

function myTimeIsBatAss(): void {
    const a = "string"
    const b = "string2"
    console.log(a + " " + b)
}

const myTimeIsBatAss2 = () => {
    const a = "string"
    const b = "string2"
    console.log(a + " " + b)
}

myTimeIsBatAss()
myTimeIsBatAss2()