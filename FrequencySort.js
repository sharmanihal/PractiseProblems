let arr=[1,1,1,1,3,2,2,4]

let map=new Map()

for(let i=0;i<arr.length;i++){
    if(map.has(arr[i])){
        map.set(arr[i], map.get(arr[i])+1)
    }else{
        map.set(arr[i],1)
    }
}
