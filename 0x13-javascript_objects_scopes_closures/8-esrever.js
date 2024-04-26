#!/usr/bin/node

exports.esrever = function (list) {
  const llength = list.length - 1;
  const newlist = [];
  for (let i = llength; i >= 0; i--) {
    newlist.push(list[i]);
  }
  return newlist;
};
