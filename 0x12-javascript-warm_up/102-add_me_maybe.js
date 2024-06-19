#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  const news = number + 1;
  theFunction(news);
};
