const {MaxHeap} = require('datastructures-js');

array=[7,10,4,3,20,15]
kk=3;
let maxHp= new MaxHeap()
let kthSmallestElement=(arr,k)=>{
    for(let i=0;i<arr.length;i++){
        maxHp.push(arr[i])
        if(maxHp.size()>k){
            maxHp.pop()
        }
    }
    return maxHp.top()
}

console.log(kthSmallestElement(array,kk))