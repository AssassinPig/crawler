var content='有一类战犯';
var encode_content = encodeURIComponent(content);
var decode_content = decodeURIComponent(encode_content);
console.log('encode_content:'+encode_content);
console.log('decode_content:'+decode_content);

//req.write('searchWord=%E6%9C%89%E4%B8%80%E7%B1%BB%E6%88%98%E7%8A%AF&searchType=name');
var search_content='searchWord='+encode_content+'&searchType=name';
console.log(search_content);
console.log(search_content.length);