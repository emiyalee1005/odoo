function my_func(v){
            document.getElementById("status"+(v*-1)).checked=!document.getElementById("status"+v).checked
            }


function remove(){

axios.request(
  {
        method: 'DELETE',
        url: '/library/todo/delete',
        data: {
    "id": document.getElementById("id").value,

  },

        transformRequest: [function (data) {
            let ret = ''
            for (let it in data) {
                ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
            }
            return ret
        }],
        headers:{'Content-Type': "application/x-www-form-urlencoded"}
    }

  ).then(
   res=>{
     if(res.data.status)
       window.location.href=window.location.origin+"/library/todo"
   }
  )
}


function submit(){
//axios.post('/library/todo/submit', {
//    "id": document.getElementById("id").value,
//    "description": document.getElementById("description").value,
//    "status": document.getElementById("status-1").checked?0:1,
//  })
//  .then(function (response) {
//    console.log(response);
//  })
//  .catch(function (error) {
//    console.log(error);
//  });


  axios.request(
  {
        method: 'POST',
        url: '/library/todo/submit',
        data: {
        ...document.getElementById("id")?{"id":document.getElementById("id").value}:{}
   ,
    "name": document.getElementById("name").value,
    "description": document.getElementById("description").value,
    "status": document.getElementById("status-1").checked?0:1,
  },

        transformRequest: [function (data) {
            let ret = ''
            for (let it in data) {
                ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
            }
            return ret
        }],
        headers:{'Content-Type': "application/x-www-form-urlencoded"}
    }

  ).then(
   res=>{
     if(res.data.status)
       window.location.href=window.location.origin+"/library/todo"
   }
  )

}


function add(){
   window.location.href=window.location.origin+"/library/todo/detail"
}

