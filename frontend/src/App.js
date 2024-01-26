import "./App.css";
import Charts from "./components/Charts";
import { Helmet } from "react-helmet";
import Form from "./components/Form";

function App() {
  return (
    <div
      className="App"
      style={{
        display: "flex",

        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <Helmet>
        <style>{"body { background-color: #f9fafb; }"}</style>
      </Helmet>
      <Charts />
      <Form />
    </div>
  );
}

export default App;
