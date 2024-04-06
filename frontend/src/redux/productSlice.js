import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  EditProduct: {},
};

export const productSlice = createSlice({
  name: "EditProduct",
  initialState,
  reducers: {
    setProductToEdit: (state, action) => {
      state.EditProduct = action.payload;
    },
  },
});

export const { setProductToEdit } = productSlice.actions;
export default productSlice.reducer;
