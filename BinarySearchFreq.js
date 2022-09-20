//Calculate Freq of 10 in arr
arr=[2,4,10,10,10,10,10,10,10,10,10,10,18,20]
let start=0;
let end=arr.length-1
let count=0;
let ele=10
while(start<=end){
    let mid=parseInt((start+end)/2)
    if(arr[mid]==ele){
        count=count+1;
        let left=mid-1;
        let rigth=mid+1
        while(arr[left]==ele){
            count=count+1;
            left=left-1
        }
        while(arr[rigth]==ele){
            count=count+1;
            rigth=rigth+1
        }
        break;
    }

    if(arr[mid]>ele){
        end=mid-1
    }else{
        start=mid+1
    }
}
console.log(count)