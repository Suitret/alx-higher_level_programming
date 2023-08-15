#!/usr/bin/node

const { dict } = require('./101-data');

const resultDict = {};

for (const userId in dict) {
  const occurrence = dict[userId];
  if (resultDict[occurrence] === undefined) {
    resultDict[occurrence] = [];
  }
  resultDict[occurrence].push(userId);
}

console.log(resultDict);
