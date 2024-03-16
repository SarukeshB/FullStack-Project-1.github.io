//                                                                      SARUKESH BOOMINATHAN

import Header from "./Header";
import Content from "./Content";
import Footer from "./Footer";
import "./App.css";
import Navbar from "./Navbar";
import NameForm from "./Input";
function App() {

  

  return (
  <div className="App-header">
  <Navbar/>
  <Header />
  <Content />
  <NameForm />
  <Footer />
  </div>
  );
}

export default App; 
