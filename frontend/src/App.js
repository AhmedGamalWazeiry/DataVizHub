import "./App.css";
import Charts from "./components/Charts";
import { Helmet } from "react-helmet";

function App() {
  return (
    <div className="App">
      <Helmet>
        <style>{"body { background-color: #f9fafb; }"}</style>
      </Helmet>
      <Charts />
    </div>
  );
}

export default App;
