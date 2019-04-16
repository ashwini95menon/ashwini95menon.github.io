import json
import webbrowser
#import django
import requests
import csv

username = "ashwini95menon"

token = "0f10ca525a26da9ec86a8471b9473f4c7398c849"

sesn = requests.session()
sessionvar=requests.session()

def list_all_repos():
    googlerepo = []
    url1 = "https://api.github.com/orgs/google/repos"
    authenticatn = sesn.get(url1, auth=(username, token))
    react_data = json.loads(authenticatn.text)
    # print(react_data)\
    for list_issues in authenticatn.json():
        googlerepo.append(list_issues['name'])

    googlerepos = list(zip(googlerepo))

    # print(googlerepo)
    return googlerepos

    ##with open('test_csv.csv', 'w') as file:

    ##    writer = csv.writer(file)
    ##    writer.writerows(googlerepos)


RepostList = list(list_all_repos())


# conert tuple to string
def convertTuple(tup):
    str = ''.join(tup)
    return str


## webpage from python
f = open('WebPage/portal.html', 'w')

message = """<!DOCTYPE html>
<html>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
 background-color: #cccccc;

}
/* The container */
.container {
  display: block;
  position: relative;
  padding-left: 35px;
  margin-bottom: 12px;
  cursor: pointer;
  font-size: 20px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
/* Hide the browser's default checkbox */
.container input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}
/* Create a custom checkbox */
.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  height: 20px;
  width: 20px;
  background-color: #eee;
}
/* On mouse-over, add a grey background color */
.container:hover input ~ .checkmark {
  background-color: #ccc;
}
/* When the checkbox is checked, add a blue background */
.container input:checked ~ .checkmark {
  background-color: #2196F3;
}
/* Create the checkmark/indicator (hidden when not checked) */
.checkmark:after {
  content: "";
  position: absolute;
  display: none;
}
/* Show the checkmark when checked */
.container input:checked ~ .checkmark:after {
  display: block;
}
/* Style the checkmark/indicator */
.container .checkmark:after {
  left: 9px;
  top: 5px;
  width: 5px;
  height: 10px;
  border: solid white;
  border-width: 0 3px 3px 0;
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}
.center {
  margin: auto;
  width: 50%;
  border: 3px solid green;
  padding: 10px;
}
.name{

  text-align: left;
    float:left;
}
.button {
  background-color: #008CBA;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}
</style>
<body>
<center>
<h1 color="blue"> GitHub Analytics </h1>
<div id="list">
<h3>Repositories</h3>
<div style="float:none; width:500px; height:200px; overflow:auto;"> 
<div class="name">
<ul>
"""

# Creating List of repositories
for val in RepostList:
    message = message + "<li style=font-size:23px; >" + convertTuple(val) + "</li>"

message = message + """</ul>
</div>
</div>
<button class="button" onclick="ShowCheckList()">Create New View</button>
</div>
<!--Check Box Starts Here -->
<div id="disp_hide" style="display:none">
<h3>Please Select Repositories:</h3>
<div style="float:none; width:500px; height:200px; overflow:auto;"> 
<div class="name">

"""

# creating checkbox repositories
for val in RepostList:
    message = message + """<label class="container"><input type="checkbox" ><label>""" + convertTuple(val) + """</label>
    <span class="checkmark"></span>
</label>"""
message = message + """</div>
</div>
 </br>
<button class="button" style="margin:10px;" onclick="Showfile();">select repos</button></br>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script>
function Showfile(){
downloadCSV({filename: "reposelect_csvfile.csv"});
var queryString = decodeURIComponent(window.location.search);
var params = {}, queries, temp, i, l;
    // Split into key/value pairs
	queryString = queryString.substring(1);
    queries = queryString.split("&");
    // Convert the array of strings into an object
    for ( i = 0, l = queries.length; i < l; i++ ) {
        temp = queries[i].split('=');
        params[temp[0]] = temp[1];
    }
    window.location.href = params[temp[0]];
};
</script>

</div>
</center>

<script type="text/javascript">
function ShowCheckList() {
  var x = document.getElementById("disp_hide");
  if (x.style.display === "none") {
    x.style.display = "block";
  } 
  var y = document.getElementById("list");
  y.style.display = "none"
}
function downloadCSV(args){
var data, filename, link;
var labelValues = $(':checkbox:checked').map(function() {
    return [$(this).next('label').text()];
}).get();
console.log(labelValues);


var csv=labelValues.join();
    filename = args.filename || 'export.csv';

    var blob = new Blob([csv], {type: "text/csv;charset=utf-8;"});

if (navigator.msSaveBlob)
{ // IE 10+
navigator.msSaveBlob(blob, filename)
}
else
{
var link = document.createElement("a");
if (link.download !== undefined)
{

// feature detection, Browsers that support HTML5 download attribute
var url = URL.createObjectURL(blob);
link.setAttribute("href", url);
link.setAttribute("download", filename);
link.style = "visibility:hidden";
document.body.appendChild(link);
link.click();
document.body.removeChild(link);
}
}
}
</script>
</body>
</html>"""
# some_var = request.POST.getlist('checks[]')
# print (some_var)
f.write(message)
f.close()

# ------------Webpage 1------------
# print(django.get_version())

f2 = open('WB1.htm', 'w')
message2 = """
<!DOCTYPE html>
<html>
<style>
body {
 background-color: #cccccc;cd

}
 /* Use case Tabs */
 .column-1 {
  float: left;
  width: 15%;
  padding: 100px;
  height: 600px; /* Should be removed. Only for demonstration */
  }

 /* buttons for different use cases*/ 
  .button {
  background-color: #008CBA;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  width: 150px;
  height: 50px;
}
</style>
<div class="column-1" style="background-color:#aaa;">
    <a href="WebPage/WB2-UC1.html"><button class="button" style="margin:30px;" name="uc1.htm">Use Case 1</button></br>
	<a href="WebPage/WB2-UC2.html"><button class="button" style="margin:30px;" id="uc2.htm">Use Case 2</button></br>
	<a href="WebPage/WB2-UC3.html"><button class="button" style="margin:30px;" id="uc3.htm">Use Case 3</button></br>

  </div>


 </HTML>"""
f2.write(message2)
f2.close()
webbrowser.open_new_tab('WB1.htm')