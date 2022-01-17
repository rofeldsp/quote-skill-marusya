const express = require("express");
const server = express();
const bodyParser = require('body-parser')
const port = process.env.PORT || 3000;
const axios = require('axios');

const createEchoResponse = require('./get_quote.js')

server.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header(
        "Access-Control-Allow-Headers",
        "Origin, X-Requested-With, Content-Type, Accept, Authorization"
    );
    res.header(
        "Access-Control-Allow-Methods",
        "GET, PATCH, PUT, POST, DELETE, OPTIONS"
    );
    next();
});


server.use(bodyParser.json());

server.use(
    bodyParser.urlencoded({
        extended: true
    })
);

server.post("/webhook",  async (req, res) => {
        let quote;
        let author;
        await axios.post(`http://api.forismatic.com/api/1.0/getQuote?method=getQuote&format=json&key=${Math.floor(Math.random() * 1000000)}`)
            .then((response) => {
                quote = response.data.quoteText;
                author = response.data.quoteAuthor;
            })
        res.json(createEchoResponse.answer(req.body, quote, author))
});

server.listen(port, () => {
    console.log("Сервер запущен на порту " + port);
});


