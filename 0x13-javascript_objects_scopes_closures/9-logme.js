#!/usr/bin/node
exports.logMe = (function (item) {
  let i = 0;
  return  function (item) { console.log(i++ + ' : ' + item): };
}());
