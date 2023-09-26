import React, {useState} from "react";

type UserType = {
    email: string;
    id: number
}


const useStateLogin = () => {
  const [email, setEmail ] = useState("")
  const [ user, setUser ] = useState<UserType | null>(null)

    const handleChangeInput = (e: React.ChangeEvent<HTMLInputElement>) => {
        e.preventDefault()
        setEmail(e.target.value);
    }

    const handleUpdateUser = (e: React.MouseEvent<HTMLButtonElement>) => {
        e.preventDefault()
        setUser({
            email: email,
            id: 1,
        })
        console.log(user, email)
    }

  return (
    <div>
      <input type="email" onChange={handleChangeInput}/>
      <button onClick={handleUpdateUser}>Enviar</button>
      { user && (<h2>{user.email}</h2>)}
    </div>
  );
};

export default useStateLogin;
