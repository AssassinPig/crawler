var http = require('http');
var cheerio = require("cheerio");

var crawler = function() { 
  this.urlQueue = new Array();
  this.urlHistory = new Array();
  this.bsfStatus = 0;
}

crawler.prototype.run = function() {
  var that = this;
  while(this.urlQueue.length) {
    console.log("=====================");

    var options = {
      hostname: 'tieba.baidu.com',
      port : 80,
      method : 'GET',
      path : this.urlQueue.shift()
    };

    var req = http.request(options, function(res) {
      console.log(options.path);
      res.setEncoding('utf8');
      var data;
      res.on('data', function (chunk) {
        data += chunk;
      });
    
      res.on('end', function(){
        that.totalData(data);
      });
    });
    
    req.on('error', function(e) {
      console.log('problem with request: ' + e.message);
    });
    
    req.end();
  } 

}

crawler.prototype.seeds = function(options) {
  this.options = options; 
  this.options.port = 80; 
  this.options.method = 'GET';
  console.log(options.hostname+options.path);
  this.urlQueue.push(options.path);
}

crawler.prototype.strategy = function(strategy) {

}

crawler.prototype.totalData = function(data) {
  var urlQueue = this.urlQueue;
  var urlHistory = this.urlHistory;
  var $ = cheerio.load(data);
  $('a').each(function(i,e){
    var href = new String($(e).attr('href'));
    if(href.match(/\/p\// )) {
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
    }
  });
}

crawler.bsf = function() {
  if(urlqueue.length) {
    return urlqueue.shift(); 
  } else {
    var newpage = pageurl+offset;
    offset += 1;
    return newpage;
  }
}

crawler.dsf = function() {

}

var options = {
    hostname: 'tieba.baidu.com',
    path: '/f?kw=%D6%D0%B3%AC&fr=ala0'
};

var crawler = new crawler();
crawler.seeds(options);
//crawler.strategy();
crawler.run();

