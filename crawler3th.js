var http = require('http');
var cheerio = require("cheerio");
var events = require('events');
var util = require('util');

var STATEGY_BSF = 1;
var STATEGY_DSF = 2;

var Crawler = function() { 
  this.urlQueue = [];
  this.urlHistory = [];
}
util.inherits(Crawler, events.EventEmitter);

Crawler.prototype.run = function() {
  var self = this;
  var options = {
    hostname: 'tieba.baidu.com',
    port : 80,
    method : 'GET',
    path : this.stategy_fun 
  };

  var req = http.request(options, function(res) {
    console.log(options.path);
    res.setEncoding('utf8');
    var data;
    res.on('data', function (chunk) {
      data += chunk;
    });
  
    res.on('end', function(){
      self.totalData(data);
    });
  });
  
  req.on('error', function(e) {
    console.log('problem with request: ' + e.message);
  });
  
  req.end();
}

Crawler.prototype.seeds = function(options) {
  this.options = options; 
  this.options.port = 80; 
  this.options.method = 'GET';
  console.log(options.hostname+options.path);
  this.urlQueue.push(options.path);
}

Crawler.prototype.set_strategy = function(strategy) {
  if(strategy == STATEGY_BSF) {
    this.strategy_fun = this.bsf;
  } 

  if(strategy == STATEGY_DSF) {
    this.strategy_fun = this.dsf;
  }
}

Crawler.prototype.totalData = function(data) {
  var self = this;
  var urlQueue = this.urlQueue;
  var urlHistory = this.urlHistory;
  var $ = cheerio.load(data);
  $('a').each(function(i,e){
    var href = new String($(e).attr('href'));
    var i=0;
    for(; i<urlHistory.length; ++i) {
      if(urlHistory[i] == href) {
        break;
      }
    }

    if(i != urlHistory.length){
      return; 
    }

    console.log(href);
    urlHistory.push(href);
    //if(href.match(/\/p\// )) {
    //}
  });
  self.run();
}

Crawler.prototype.strategy = function() {
 return strategy_fun; 
}

Crawler.prototype.bsf = function() {
  return urlqueue.shift(); 
}

Crawler.prototype.dsf = function() {
  return urlqueue.pop(); 
}

var options = {
    hostname: 'tieba.baidu.com',
    path: '/f?kw=%D6%D0%B3%AC&fr=ala0'
};

var crawler = new Crawler();
crawler.seeds(options);
crawler.set_strategy(STATEGY_BSF);
crawler.run();

