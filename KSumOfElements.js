const {MaxHeap} = require('datastructures-js');
const arr=[1,3,12,5,15,11]
let minheap= new MaxHeap()
let k1=3
let k2=6;

for(let i=0;i<arr.length;i++){
    minheap.push(arr[i])
    if(minheap.size()>k1){
        minheap.pop()
    }
}
let first= minheap.pop()
minheap.clear();

for(let i=0;i<arr.length;i++){
    minheap.push(arr[i])
    if(minheap.size()>k2){
        minheap.pop()
    }
}
let second= minheap.pop()
let sum=0
for(let i=0;i<arr.length;i++){
    if(arr[i]>first && arr[i]<second){
sum+=arr[i]
    }
}
console.log(sum)