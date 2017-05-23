///* --> nodeadmin.js file <-- */////
'use strict'
var express = require('express');
//var mysql = require('mysql');
//var mysqltorest  = require('mysql-to-rest');
var app = express();
 
// add the nodeadmin middleware
var nodeadmin = require('nodeadmin');
//var api = mysqltorest(app,connection);
app.use(nodeadmin(app));
 
//Let Nodeadmin listen to Port 3333
app.listen(3333);
