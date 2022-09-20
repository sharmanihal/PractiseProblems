const maxAreaBinaryArray=(arr,n,m)=>{
    
    let firstRow=[...arr[0]]
    let vector=[arr[0]];
    for(let i=1;i<m;i++){
        let temp=[q         ]
        for(let j=0;j<n;j++){
            firstRow[j]=firstRow[j]*arr[i][j]
            firstRow[j]=firstRow[j]+arr[i][j]
            temp.push(firstRow[j])
        }
        vector.push(temp)
    }
    let maxArea=0
    
    for(let i=0;i<vector.length;i++){
        let temp=(maxAreaOfHistogram(vector[i],vector[i].length))
        if(maxArea<temp){
            maxArea=temp
        }
    }
    return maxArea;
}

const maxAreaOfHistogram=(arr,n)=>{

    const right=nsr(arr,n)
    const left = nsl(arr,n)
  
    let maxArea=0;
    let width=[]
    for(let i=0;i<n;i++){
        width[i]= right[i]-left[i]-1
    }
    for(let i=0;i<n;i++){
        if(maxArea< width[i]* arr[i]){
            maxArea= width[i]*arr[i]
        }
    }
    return maxArea;
}

const nsr=(arr,n)=>{
    let vector=[]
    let stack=[]

    for(let i=n-1;i>=0;i--){
        if(stack.length==0){
            vector.push(n)
        }else if(stack.length>0 && stack[stack.length-1].element<arr[i]){
            vector.push(stack[stack.length-1].index)
        }else if(stack.length>0 && stack[stack.length-1].element>=arr[i]){
            while(stack.length >0 && stack[stack.length-1].element>=arr[i]){
                stack.pop()
            }
            if(stack.length==0){
                vector.push(n)
            }else{
                vector.push(stack[stack.length-1].index)
            }
        }
        stack.push({element:arr[i],index:i})
    }
    return vector.reverse()
}


const nsl=(arr,n)=>{
    let vector=[]
    let stack=[]

    for(let i=0;i<n;i++){
        if(stack.length==0){
            vector.push(-1)
        }else if(stack.length>0 && stack[stack.length-1].element<arr[i]){
            vector.push(stack[stack.length-1].index)
        }else if(stack.length>0 && stack[stack.length-1].element>=arr[i]){
            while(stack.length >0 && stack[stack.length-1].element>=arr[i]){
                stack.pop()
            }
            if(stack.length==0){
                vector.push(-1)
            }else{
                vector.push(stack[stack.length-1].index)
            }
        }
        stack.push({element:arr[i],index:i})
    }
    return vector
}







console.log(maxAreaBinaryArray([[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]],5,4))