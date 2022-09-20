const {MaxHeap} = require('datastructures-js');
arr=[5,6,7,8,9]
k=3
x=7
let maxHeap=new MaxHeap()
let KClosestNumber=(array,kk,xx)=>{
    for(let i=0;i<array.length;i++){
        let abs= Math.abs(array[i]-xx)
        maxHeap.push(abs,array[i])
        if(maxHeap.size()>kk){
            maxHeap.pop()
        }
    }
    return maxHeap._heap;
}
console.log(KClosestNumber(arr,k,x))