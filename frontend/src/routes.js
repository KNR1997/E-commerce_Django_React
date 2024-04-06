import React from "react";
import { Route, Routes } from "react-router-dom";
import MainLayout from './layouts/MainLayout';
import About from "./pages/About/About";
import SignIn from "./pages/Account/SignIn";
import SignUp from "./pages/Account/SignUp";
import Cart from "./pages/Cart/Cart";
import Contact from "./pages/Contact/Contact";
import Home from "./pages/Home/Home";
import Journal from "./pages/Journal/Journal";
import Offer from "./pages/Offer/Offer";
import Payment from "./pages/payment/Payment";
import ProductDetails from "./pages/ProductDetails/ProductDetails";
import Shop from "./pages/Shop/Shop";

const routes = (
  <Route>
    <Route path="/" element={<MainLayout />}>
      {/* ==================== Header Navlink Start here =================== */}
      <Route index element={<Home />} />
      <Route path="/shop" element={<Shop />} />
      <Route path="/about" element={<About />} />
      <Route path="/contact" element={<Contact />} />
      <Route path="/journal" element={<Journal />} />
      {/* ==================== Header Navlink End here ===================== */}
      <Route path="/category/:category" element={<Offer />} />
      <Route path="/product/:_id" element={<ProductDetails />} />
      <Route path="/cart" element={<Cart />} />
      <Route path="/paymentgateway" element={<Payment />} />
    </Route>
    <Route path="/signup" element={<SignUp />} />
    <Route path="/signin" element={<SignIn />} />
  </Route>
);

export default routes;
