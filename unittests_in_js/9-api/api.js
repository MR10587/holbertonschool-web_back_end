const express = require("express");
const app = express();

const port = 7865;

app.get("/", (req, res) => {
  res.send("Welcome to the payment system");
});

app.get("/card/:id", (req, res) => {
  let id = Number(req.params.id);

  if (Number.isInteger(id)) {
    res.send(`Payment methods for card ${id}`);
  } else {
    res.sendStatus(404);
  }
});

if (require.main === module) {
  app.listen(port, () => {
    console.log(`API available on localhost port ${port}`);
  });
}

module.exports = app;
