/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        if (functions.length === 0) {
            resolve([]);
            return;
        }
        
        const results = new Array(functions.length);
        let completed = 0;
        
        functions.forEach((fn, i) => {
            fn()
                .then(val => {
                    results[i] = val;
                    completed++;
                    if (completed === functions.length) {
                        resolve(results);
                    }
                })
                .catch(err => reject(err));
        });
    });
};
