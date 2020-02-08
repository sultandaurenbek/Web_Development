
// delete button x (u00D7)

var myNodelist = document.getElementsByTagName("LI");
var i;
for (i = 0; i < myNodelist.length; i++) {
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "btn_delete";
  span.appendChild(txt);
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
list.addchoose_objentListener('click', function(choose_obj) {
  if (choose_obj.target.tagName === 'LI') {
    choose_obj.target.classList.toggle('choose');
  }
}, false);

// creating a new item  int the list when clicking on the "Add" button
function addElement() {
  var li = document.createElement("li");
  var inputText = document.getElementById("txt-input").value;
  var t = document.createTextNode(inputText);
  li.appendChild(t);
  if (inputText === '') {
    alert("You need to write something!");
  } else {
    document.getElementById("myUL").appendChild(li);
  }
  document.getElementById("txt-input").value = "";
  
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "btn_delete";
  span.appendChild(txt);
  li.appendChild(span);

  for (i = 0; i < btn_delete.length; i++) {
    btn_delete[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}
