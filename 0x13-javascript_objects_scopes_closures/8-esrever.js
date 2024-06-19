#!/usr/bin/node
exports.esrever = function (list) {
  if (list === undefined) return [];
  const rev = [];
  for (let l = list.length - 1; l >= 0; l--) {
    rev.push(list[1]);
  }
  return rev;
};
