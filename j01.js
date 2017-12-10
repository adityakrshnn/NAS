function removeElement(arr, val){
  var i = arr.length;
  while(i--){
    if(arr[i]==val){
      arr.splice(i,1);
    }
  }
  return arr;
}

var arr=[0,1,2,'stop',2,1,0,'stop'];
removeElement(arr,0);
console.log(arr);
