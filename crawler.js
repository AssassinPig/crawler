var http = require('http');
var cheerio = require("cheerio");
var options = {
  hostname: 'tieba.baidu.com',
  port: 80,
  path: '/f?kw=%D6%D0%B3%AC&fr=ala0',
  method: 'GET'
}

var pageUrl = '/f?kw=%D6%D0%B3%AC&pn=';
var urlQueue = new Array(); 
var offset = 1;
var urlHistory = new Array();
var bsfStatus = 0;

urlHistory.push(options.path);
urlQueue.push(options.path);
download(options);

function bsf() {
  if(urlQueue.length) {
    return urlQueue.shift(); 
  } else {
    var newPage = pageUrl+offset;
    offset += 1;
    return newPage;
  }
}

function totalData(data) {
  //console.log(data);
  var $ = cheerio.load(data);
  $('a').each(function(i,e){
    var href = new String($(e).attr('href'));
    if(href.match(/\/p\// )) {
      console.log(href);
      var i=0;
      for(; i<urlHistory.length; ++i) {
        if(urlHistory[i] == href) {
          break;
        }
      }

      if(i != urlHistory.length){
        return; 
      }

      urlHistory.push(options.path);
      if(!bsfStatus) {
        options.path = href;
      } else {
        options.path = bsf();
      }

      if(options.path) {
        download(options);
      }
    }
  });
}

function download(options) { 
  var req = http.request(options, function(res) {
    console.log("=====================");
    console.log(options.path);
    //console.log('STATUS: ' + res.statusCode);
    //console.log('HEADERS: ' + JSON.stringify(res.headers));
    res.setEncoding('utf8');
    var data;
    res.on('data', function (chunk) {
      data += chunk;
    });
  
    res.on('end', function(){
      totalData(data);
    });
  });
  
  req.on('error', function(e) {
    console.log('problem with request: ' + e.message);
  });
  
  req.end();
}
