const {MinHeap} = require('datastructures-js');

arr=[6,5,3,2,8,10,9]
k=3;
let minheap=new MinHeap()
let index=0
let KSortedArray=(array,kk)=>{
    for(let i=0;i<array.length;i++){
        minheap.push(array[i])
        if(minheap.size()>k){
            array[index]=minheap.pop()
            index=index+1;
        }
    }
    while(minheap.size()>0){
        array[index]=minheap.pop()
        index=index+1
    }
    return array;
}

console.log(KSortedArray(arr,k))