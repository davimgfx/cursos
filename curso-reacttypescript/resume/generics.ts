// Generics - Clean Code

interface IAuthor {
    id: number;
    username: string;
}

interface ICategory{
    id: number;
    title: string;
}

interface IPost {
    id: number;
    title: string;
    desc: string;
    extra: IAuthor[] | ICategory[]
}

interface IPostCategory<T> {
    id: number;
    title: string;
    desc: string;
    extra: T[]
}

const callTheAPI : IPostCategory<string> = {
    id: 12345,
    title: "Mamos",
    desc: "A little song",
    extra: ["Pagode", "Samba"]
}

console.log(callTheAPI.extra)

