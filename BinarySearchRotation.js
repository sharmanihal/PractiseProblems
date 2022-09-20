// find how many times the arr was roatated
arr=[2,1]
let start=0;
let end=arr.length-1;
let rotation =0
let n=arr.length
while(start<=end){
    let mid= parseInt((start+end)/2)
    let prev=(mid+n-1)%n;
    let next=(mid+1)%n;
    if(prev>arr[mid] && next>arr[mid]){
        rotation=mid;
    }
    if(arr[mid]<=arr[end]){
        end=mid-1
    }
    if(arr[start]<arr[mid]){
        start=mid+1;
    }
}
console.log(rotation)