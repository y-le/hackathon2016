var express = require("express");
var bodyParser = require("body-parser");
var app = express();

app.use(bodyParser.urlencoded({extended : true}));

app.post("/pathpostdataissentto", function(request, response) {
  console.log(request.body);
  //Or
  console.log(request.body.fieldName);
});

app.listen(8080);
