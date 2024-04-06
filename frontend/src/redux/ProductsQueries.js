import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

// Function to get access token from local storage
const getAccessToken = () => {
    const authTokens = localStorage.getItem("authTokens");
    if (authTokens) {
      const tokens = JSON.parse(authTokens);
      return tokens.access; // Assuming the access token key is 'access_token'
    }
    return null;
};

export const useApiProductsSlice = createApi({
  reducerPath: "api",
  baseQuery: fetchBaseQuery({ baseUrl: process.env.REACT_APP_DEV_URL }),
  tagTypes: ["Products"],
  endpoints: (builder) => ({
    getProducts: builder.query({
      query: () => ({
        url: "/api/products",
        headers: {
          Authorization: `Bearer ${getAccessToken()}`,
        },
      }),
      // transformResponse: (res) => res.sort((a, b) => b.id - a.id),
      providesTags: ["Products"],
    }),

    addProduct: builder.mutation({
      query: (product) => ({
        url: "/api/products",
        method: "POST",
        headers: {
          Authorization: `Bearer ${getAccessToken()}`,
        },
        body: product,
      }),
      invalidatesTags: ["Products"],
    }),

    updateProduct: builder.mutation({
      query: (product) => ({
        url: `/api/products/${product.id}`,
        method: "PUT",
        headers: {
          Authorization: `Bearer ${getAccessToken()}`,
        },
        body: product,
      }),
      invalidatesTags: ["Products"],
    }),

    deleteProduct: builder.mutation({
      query: (id) => ({
        url: `/api/product/${id}`,
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${getAccessToken()}`,
        },
        body: id,
      }),
      invalidatesTags: ["Products"],
    }),
  }),
});

export const {
  useGetProductsQuery,
  useAddProductMutation,
  useUpdateProductMutation,
  useDeleteProductMutation,
} = useApiProductsSlice;
