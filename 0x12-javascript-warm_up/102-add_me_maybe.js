#!/usr/bin/node
module.exports = {
    addMeMaybe: function (n, fun) {
        return (fun(n + 1));
    }
};
