import React, { useState } from "react";
import { ImCross } from "react-icons/im";
import { useDispatch } from "react-redux";
import {
  deleteItem,
  drecreaseQuantity,
  increaseQuantity,
} from "../../redux/orebiSlice";
import { setProductToEdit } from "../../redux/productSlice";
import { useNavigate } from "react-router-dom";
import {
  newArrOne,
  newArrTwo,
  newArrThree,
  newArrFour,
} from "../../assets/images/index";
import { useDeleteProductMutation } from "../../redux/ProductsQueries";

const MyProductCard = ({ item }) => {
  const [openEditProductForm, setOpenEditProductForm] = useState(false);
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [deleteProduct] = useDeleteProductMutation();

  const handleEditProduct = () => {
    dispatch(setProductToEdit(item));
    navigate("/edit-product");
  };

  const handleDeleteProduct = () => {
    console.log("handle edit product");
    deleteProduct(item.id);
  };

  console.log(item);

  return (
    <div className="w-full grid grid-cols-5 mb-4 border py-2">
      <div className="flex col-span-5 mdl:col-span-2 items-center gap-4 ml-4">
        {/* <ImCross
          onClick={() => dispatch(deleteItem(item._id))}
          className="text-primeColor hover:text-red-500 duration-300 cursor-pointer"
        /> */}
        <img className="w-32 h-32" src={newArrOne} alt="productImage" />
        <h1 className="font-titleFont font-semibold">{item.name}</h1>
      </div>
      <div className="col-span-5 mdl:col-span-3 flex items-center justify-between py-4 mdl:py-0 px-4 mdl:px-0 gap-6 mdl:gap-0">
        <div className="flex w-1/3 items-center text-lg font-semibold">
          ${item.price}
        </div>
        <div className="w-1/3 flex items-center gap-6 text-lg">
          <p>{item.quantity}</p>
        </div>
        {/* <div className="w-1/3 flex items-center font-titleFont font-bold text-lg">
          <p>${item.quantity * item.price}</p>
        </div> */}
        <button onClick={handleEditProduct}>Edit</button>
        <button onClick={handleDeleteProduct}>Delete</button>
      </div>
    </div>
  );
};

export default MyProductCard;
