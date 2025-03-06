/*
npm i express
npm i eventsource
*/

const http = require("http");
const fs = require("fs");
const express = require("express");
const app = express();

// Serve static files
app.use(express.static("./"));

// Example addizionatore
app.get("/api", (req, res) => {
  //Per leggere gli elementi di query: req.query.<nome chiave>
  // GET /api?add1=10&add2=20&username=user01
  let add1 = req.query["add1"];
  let add2 = req.query["add2"];
  let user = req.query["username"];
  if (user === "user01") {
    res.json({ risposta: add1 + add2 });
  } else {
    res.json({ risposta: add2 + add1 });
  }
});

// Example abilitatore
app.get("/abilita", (req, res) => {
  //Per leggere gli elementi di query: req.query.<nome chiave>
  // GET /abilita?admin=dimitri&utente=arcieri
  let admin = req.query["admin"];
  let utente = req.query["utente"];
  res.json({ risposta: "OK" });
});

let options = {};

let host = "10.46.8.128";
let port = 3000;

http.createServer(options, app).listen(port, host, () => {
  console.log("HTTP server running at http://localhost:3000");
});
