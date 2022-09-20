const rainWaterTrapping=(arr,n)=>{
    let left=mal(arr,n)
    let right = mar(arr,n)
    console.log(left,right)
    let water=0
    for(let i=0;i<n;i++){
        water+=Math.min(left[i],right[i])-arr[i]
    }
    return water;
}
const mal=(arr,n)=>{
    let left=[]
    for(let i=0;i<n;i++){
        if(i==0){
            left.push(arr[0])
        }
        else if(left[i-1]>arr[i]){
            left.push(left[i-1])
        }else{
            left.push(arr[i])
        }
    }
    return left
}

const mar=(arr,n)=>{
    let right=[]
    for(let i=n-1;i>=0;i--){
        if(i==n-1){
            right.push(arr[n-1])
        }
        else if(right[n-2-i]>arr[i]){
            right.push(right[n-2-i])
        }else{
            right.push(arr[i])
        }
    }
    return right.reverse()
}
console.log(rainWaterTrapping([3,0,5,2,0,4],6))

