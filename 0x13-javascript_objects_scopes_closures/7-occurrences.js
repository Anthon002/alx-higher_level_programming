#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, element) => count + (element === searchElement ? 1 : 0), 0);
};
