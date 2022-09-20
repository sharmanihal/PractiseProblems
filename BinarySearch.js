//first and last occurrence of 10
//   0 1 2 3   4  5 6   7  8
arr=[2,4,8,9,10,10,11,11,11,11,14,24]

let start=0;
let end= arr.length-1;
let ele=10;
let index=-1
while(start<=end){
    let mid=parseInt((start+end)/2);
    if(arr[mid]==ele){
        index=mid;
        end=mid-1;
       
    }
    if(arr[mid]>ele){
        end=mid-1
    }else if(arr[mid]<ele){
        start=mid+1
    }
}


// index=-1;
// //last occurrance
// while(start<=end){
//     let mid=parseInt((start+end)/2);
//     if(arr[mid]==ele){
//         index=mid;
//         start=mid+1;
       
    
//     }
//     if(arr[mid]>ele){
//         end=mid-1
//     }else if(arr[mid]<ele){
//         start=mid+1
//     }
// }
console.log(index)