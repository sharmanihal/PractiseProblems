const maxAreaHistogram=(height,n)=>{
    const right= nsr(height,n)
    const left =nsl(height,n)
    let maxArea=0;
    let width=[]
    for(let i=0;i<n;i++){
        width[i]= right[i]-left[i]-1
    }
    for(let i=0;i<n;i++){
        if(maxArea< width[i]* height[i]){
            maxArea= width[i]*height[i]
        }
    }
    return maxArea;
}

const nsr=(height,n)=>{
    const vector =[]
    const stack=[]

    for(let i=n-1;i>=0;i--){
        if(stack.length==0){
            vector.push(n)
        }
        else if(stack.length>0 && stack[stack.length-1].element<height[i]){
            vector.push(stack[stack.length-1].index)
        }else if(stack.length>0 && stack[stack.length-1].element>=height[i]){
            while(stack.length>0 && stack[stack.length-1].element>=height[i]){
                stack.pop();
            }
            if(stack.length==0){
                vector.push(n)
            }else{
                vector.push(stack[stack.length-1].index)
            }
        }
        stack.push({element:height[i],index:i})
    }
    return vector.reverse()
}
const nsl=(height,n)=>{
    const stack=[]
    const vector=[];
    for(let i=0;i<n;i++){
        if(stack.length==0){
            vector.push(-1)
        }else if(stack.length>0 && stack[stack.length-1].element<height[i]){
            vector.push(stack[stack.length-1].index)
        }else if(stack.length>0 && stack[stack.length-1].element>=height[i]){
            while(stack.length>0 && stack[stack.length-1].element>=height[i]){
                stack.pop();
            }
            if(stack.length==0){
                vector.push(-1)
            }else{
                vector.push(stack[stack.length-1].index)
            }
        }
        stack.push({element:height[i],index:i})
    }
    return vector;
}
console.log(maxAreaHistogram([6,2,5,4,5,1,6],7))