#!/usr/bin/node
// Print Javascript is amazing

function callMeMoby (x, fun) {
  for (let i = 0; i < x; i++) {
    fun();
  }
}

module.exports = {
  callMeMoby
};
