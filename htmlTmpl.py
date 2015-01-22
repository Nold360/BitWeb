#!/usr/bin/env python2

# Copyright (C) 2014 Johannes Schwab

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

header = """
<!DOCTYPE html>
<html>
<head>
<title>Bitmessage</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name="viewport" content="width=device-width"; />

<link rel="icon" type="image/x-icon" href="favicon.ico" />
<link rel="shortcut icon" type="image/x-icon" href="favicon.ico" />
<link type="image/x-icon" href="favicon.ico" />

<style>
body {
    color: #2B2B2B;
    background-color: #FDFDFD;
    text-align: center;
    line-height: 1.5;
    padding: 0px;
    margin: 0px;
}

a {
    cursor: pointer;
}

a, input.button, select {
    white-space: nowrap;
    color: #FFFFFF;
    background-color: #8e9294;
    text-decoration: none;
    font-weight: bold;
    padding: 1px 5px 1px 5px;
    margin-left: 4px;
    border: none;
    border-radius: 5px;
    background-image: linear-gradient(to bottom, #8e9294, #000000);
}

input {
    margin-right: 4px;
}

div {
    text-align: left;
}

div.msgHeaderRead {
    padding: 2px;
    margin: 5px;
    background: #DFE2E8;
    background: linear-gradient(#FCFCFC, #DFE2E8);
}

div.msgHeaderUnread {
    color: #000000;
    background-color: #DFE2E8;
    font-weight: bold;
    padding: 2px;
    margin: 5px;
}

div.msgText {
    margin: 1px;
    padding: 3px;
    margin-top: 10px;
    background-color: #FCFCFC;
    line-height: 1;
    border: 1px solid #DFE2E8;
}

div.msgBody, div.addrbookentry, div.subscription {
    background-color: #DFE2E8;
    background: linear-gradient(#DFE2E8, #DCDCDC);
    padding: 2px;
    margin: 5px;
    margin-bottom: 10px;
}

div.addrbookentry, div.subscription {
    background: linear-gradient(#FCFCFC, #DFE2E8);
}

div.label {
    border-bottom: 1px solid lightgrey;
    font-weight: bold;
}

div.label a {
    font-weight: normal;
    float: right;
    padding: 0px 2px 0px 2px;
}

form {
    line-height: 2;
}

hr {
    color: #2B2B2B;
    background-color: #2B2B2B;
    height: 4px;
    border: none;
}

ul {
    margin: 0;
    padding: 0;
}

#title {
    float: left;
    color: #000000;
    display: inline;
    padding: 8px 15px;
    font-size: large;
    background: none;
}

#title a, #title a:hover {
    color: black;
    text-shadow: #FFFFFF 0px 1px 0px;
    background: none;
}

#navigation {
    width: 100%;
    text-align: center;
    list-style: none;
    color: #7E838A;
    padding: 8px 0px;
    margin-top: 0px;
    background: #B5B9C1;
    background: linear-gradient(#FCFCFC, #DFE2E8);
}

#navigation li {
    display: inline;
}

#navigation a {
    color: #5E535A;
    background: none;
    margin: 5px;
    padding: 8px 15px;
    text-shadow: #FFF 0px 1px 0px
    font-family: Helvetica,Arial,sans-serif;
    font-weight: normal;
}

#navigation a:hover {
    color: #000000;
}

#container {
    width:80%;
    text-align: center;
}

@media screen and (max-width : 600px) {
    #navigation, lu {
         width: 100%;
         float: left;
         padding: 0px 0px;
         background: none;
    }
    #navigation li, #navigation a {
        display: block;
        width: 100%;
        float: left;
        padding: 2px 0px;
        margin: 0px 0px;
        background: linear-gradient(#FCFCFC, #DFE2E8);
    }

    #title {
        text-align: center;
        padding: 8px 0px;
        margin-bottom: 5px;
        display: block;
        width: 100%;
        background: linear-gradient(#FCFCFC, #DFE2E8);
    }

    #container {
        width:100%;
    }
}


</style>

<script type="text/javascript">
function callback(url, params) {
    if (window.XMLHttpRequest) {
       http = new XMLHttpRequest();
    } else if (window.ActiveXObject) {
       http = new ActiveXObject("Microsoft.XMLHTTP");
    }
    if (http != null) {
       http.open("GET", url + "?" + params, true);
       http.send(null);
    }
}

function markRead(id) {
    header = document.getElementById("H-" + id);
    if (header.className.match(/(?:^|\s)msgHeaderUnread(?!\S)/)) {
        header.className = 'msgHeaderRead';
        callback("markread", "msgid=" + id);
    }
}

function markUnread(id) {
    header = document.getElementById("H-" + id);
    if (header.className.match(/(?:^|\s)msgHeaderRead(?!\S)/)) {
        header.className = 'msgHeaderUnread';
        callback("markunread", "msgid=" + id);
    }
}

function delMsg(id) {
    callback("delmsg", "msgid=" + id);
    document.getElementById("H-" + id).style.display = 'none';
    document.getElementById(id).style.display = 'none';
}

function delSentMsg(id) {
    callback("delsentmsg", "msgid=" + id);
    document.getElementById("H-" + id).style.display = 'none';
    document.getElementById(id).style.display = 'none';
}

function ShowHideDiv(id) {
    obj = document.getElementById(id);
    if (obj.style.display == 'none') {
        obj.style.display = 'block';
        markRead(id);
    } else {
        obj.style.display = 'none';
    }
}

function HideMessages() {
    obj = document.getElementsByClassName("msgBody");
    for (i in obj) {
        if (obj[i].style != undefined) {
            obj[i].style.display = 'none';
        }
    }
}

function broadcastMsg(brd) {
    document.getElementById("to").disabled = brd;
}

function sendForm(id, conf = false) {
    if (conf) {
        if (! confirm(conf)) return false;
    }
    document.forms[id].submit();
}

</script>

</head>

<body>
    <div id="title"><a href="https://github.com/ddorian1/BitWeb" target="_blank">BitWeb</a></div>
    <ul id="navigation">
        <li><a href="inbox" class="menu">Inbox</a></li>
        <li><a href="outbox" class="menu">Outbox</a></li>
        <li><a href="composer" class="menu">New message</a></li>
        <li><a href="subscriptions" class="menu">Subscriptions</a></li>
        <li><a href="chans" class="menu">Chans</a></li>
        <li><a href="addressbook" class="menu">Address book</a></li>
        <li><a href="identities" class="menu">Your identities</a></li>
        <li><a href="status" class="menu">Connection status</a></li>
        <li><a href="logout" class="menu">Logout</a></li>
    </ul>
<center>
<div id='container'>
"""

footer = """
</div>
</center>
<script type="text/javascript">
if (document.getElementById("focus")) {
    document.getElementById("focus").focus();
}
HideMessages();
</script>
</body>
</html>
"""

class HTMLPage():
    def __init__(self):
        self.data = u""

    def addLine(self, line, withBr = True):
        self.data += line
        if withBr:
            self.data += u"<br />"
            self.data += u"\n"

    def getPage(self):
        page = header + self.data + footer
        return page.encode('utf-8')
