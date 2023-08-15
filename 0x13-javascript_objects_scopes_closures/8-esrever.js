#!/usr/bin/node

exports.esrever = function (list) {
  const reversedArray = list.reduce((acc, current) => [current, ...acc], []);
  return reversedArray;
};
