const express = require("express");
const bodyParser = require("body-parser");
const process = require("node:process");

const app = express();
const HOST = process.env.HOST ?? "localhost";
const PORT = process.env.PORT ?? "28888";
const FLAG = process.env.FLAG ?? "TsukuCTF25{dummy_flag}";

app.use(bodyParser.urlencoded({ extended: true }));

function chall(str = "[1, 2, 3]") {
  const sanitized = str.replaceAll(" ", "");
  if (sanitized.length < 10) {
    return `error: no flag for you. sanitized string is ${sanitized}, length is ${sanitized.length.toString()}`;
  }
  const array = JSON.parse(sanitized);
  if (array.length < 0) {
    // hmm...??
    return FLAG;
  }
  return `error: no flag for you. array length is too long -> ${array.length}`;
}

app.get("/", (_, res) => {
  res.send(
    `How to use -> curl -X POST -d 'array=[1,2,3,4]' http://${HOST}:${PORT}\n`,
  );
});

app.post("/", (req, res) => {
  const array = req.body.array;
  res.send(chall(array));
});

app.listen(PORT, () => {
  console.log(`Server is running on http://${HOST}:${PORT}`);
});
