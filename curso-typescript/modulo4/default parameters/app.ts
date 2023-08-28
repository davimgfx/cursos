function thisIsMyName(name: string, value: number = 0): void {
    console.log(`Meu nome é ${name} ${value !== undefined ? `,esse é meu valor ${value}` : ""}`);
    console.log(value);
}

thisIsMyName("davi");
