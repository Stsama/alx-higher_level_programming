#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nbre = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) { nbre += 1; }
  }
  return nbre;
};
