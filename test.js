const obj = {}
const a = (num)=>{
    if (num===1){
        return 'one'
    } else if (num===2){
        return 'two'
    }
    return 'not num'
}

obj[a(1)] = ['1','2','3']
obj[a(2)] = [a(1)]

console.log(obj)


