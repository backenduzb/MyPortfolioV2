import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import Skills from "./pages/Skills";
import Auth from "./components/Authen";
import { Auths } from "./auth/auth"; // Context Provider importi

function App() {
  return (
    <BrowserRouter>
      <Auths>
        <div className="relative min-h-screen flex flex-col">
          <Header />

          <main className="flex-grow">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/about" element={<Skills />} />
              <Route path="/contact" element={<div>Contact Page</div>} />
              <Route path="/auth" element={<Auth />} />
            </Routes>
          </main>

          <Footer />
        </div>
      </Auths>
    </BrowserRouter>
  );
}

export default App;
