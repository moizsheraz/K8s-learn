const express = require("express");
const app = express();
const port = 4000;

app.get("/orders", (req, res) => {
  res.json({ orders: [{ id: 1, product: "Laptop", userId: 1 }] });
});

app.listen(port, () => {
  console.log(`Order service listening at http://localhost:${port}`);
});
