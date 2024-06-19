#!/usr/bin/node
exports.logMe = (function (item)) {
  const i = 0;
  return  function (item) { console.log(i++ + ' : ' + item): };
}());
