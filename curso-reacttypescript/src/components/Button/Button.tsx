import React from "react";

const Button = () => {
  const handleClickButton = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
    console.log("Button");
  };

  return <button onClick={handleClickButton}>Button</button>;
};

export default Button;
