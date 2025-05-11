const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const app = express();
app.use(bodyParser.text());

app.post('/', (req, res) => {
  try {
    if (req.body.includes('flag')) {
      return res.status(403).send('Not allowed!');
    }
    if (req.body.includes('\\') || req.body.includes('/')
      || req.body.includes('!!') || req.body.includes('<')) {
      return res.status(403).send('Hello, Hacker :)');
    }
    const data = yaml.load(req.body);
    const filePath = data.file;

    if (filePath && fs.existsSync(filePath)) {
      const content = fs.readFileSync(filePath, 'utf8');
      return res.send(content);
    } else {
      return res.status(404).send('File not found');
    }
  } catch (err) {
    return res.status(400).send('Invalid request');
  }
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
