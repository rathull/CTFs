const readR1cs = require("r1csfile").readR1cs
// import readR1cs from "r1csfile.js"

readR1cs("flag_constraints.r1cs").then((r1cs) => {
	console.log(r1cs);
});