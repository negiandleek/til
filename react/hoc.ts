import React, { useEffect, useState } from "react";

type Container = {
  initialValue: number;
};

type Presentation = {
  value: number;
  onClick: () => void;
};

type Hoc = (
  Component: React.FC<Presentation>
) => (props: Container) => React.ReactElement<any, any>;

const Compose: Hoc = Component =>
  function Hoge({ initialValue }) {
    const [state, setState] = useState(initialValue);
    const handleClick = () => {
      setState(prev => prev + 1);
    };
    useEffect(() => {
      console.log("useEffect");
    }, []);
    return <Component value={state} onClick={handleClick} />;
  };

const Dom: React.FC<Presentation> = ({ value, onClick }) => {
  return (
    <div>
      test: {value}
      <div>
        <button onClick={onClick}>button</button>
      </div>
    </div>
  );
};

export default Compose(Dom);
