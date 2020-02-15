
// delete button x (u00D7)

var myNodelist = document.getElementsByTagName("LI");
var i;
for (i = 0; i < myNodelist.length; i++) {

 var span = document.createElement("IMG");
        span.setAttribute("src","https://cdn2.iconfinder.com/data/icons/e-business-helper/240/627249-delete3-512.png");
        span.setAttribute("width","15px");
        span.setAttribute("align","right");
        span.className = "btn_delete";
        document.body.appendChild(span);
        myNodelist[i].appendChild(span);
}

var btn_delete = document.getElementsByClassName("btn_delete");
var i;
for (i = 0; i < btn_delete.length; i++) {
  btn_delete[i].onclick = function() {
    var div = this.parentElement;
    div.style.display = "none";
}
}

// Add a "choose" symbol when clicking on a list item
var list = document.querySelector('ul');
list.addEventListener('click', function(choose_obj) {
  if (choose_obj.target.tagName === 'LI') {
    choose_obj.target.classList.toggle('choose');
  }
}, false);

// creating a new item  int the list when clicking on the "Add" button
function addElement() {
  var inputText = document.getElementById("txt-input").value;

  if (inputText === '') {
    alert("You need to write something!");
  }
  else{

  var li = document.createElement("li");
  var t = document.createTextNode(inputText);
  li.appendChild(t);
document.getElementById("myUL").appendChild(li);

document.getElementById("txt-input").value = "";
  
var span = document.createElement("IMG");
        span.setAttribute("src","https://cdn2.iconfinder.com/data/icons/e-business-helper/240/627249-delete3-512.png");
        span.setAttribute("width","15px");
        span.setAttribute("align","right");
        span.className = "btn_delete";
        document.body.appendChild(span);
        myNodelist[i].appendChild(span);

      
      
  for (i = 0; i < btn_delete.length; i++) {
    btn_delete[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
    
    }
  }
}
