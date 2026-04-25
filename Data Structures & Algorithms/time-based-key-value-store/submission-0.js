class TimeMap {
    constructor() {
        this.keyStore = new Map();
    }

    /**
     * @param {string} key
     * @param {string} value
     * @param {number} timestamp
     * @return {void}
     */
    set(key, value, timestamp) {
        if (!this.keyStore.has(key)) {
            this.keyStore.set(key, []);
        }
        this.keyStore.get(key).push([timestamp, value]);       
    }

    /**
     * @param {string} key
     * @param {number} timestamp
     * @return {string}
     */
    get(key, timestamp) {
        if(!this.keyStore.has(key))
            return "";
        
        let store = this.keyStore.get(key);
        let start = 0
        let end = store.length - 1;
        let res = "";
        while(start <= end) {
            let middle = Math.floor(start + (end - start) / 2);
            if (store[middle][0] <= timestamp) {
                res = store[middle][1];
                start = middle + 1;
            } else {
                end = middle - 1;
            }
        }
        return res;
    }
}
