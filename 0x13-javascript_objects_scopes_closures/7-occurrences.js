#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let cpt = 0;
  for (const element of list) {
    if (element === searchElement) { cpt++; }
  }
  return cpt;
};
