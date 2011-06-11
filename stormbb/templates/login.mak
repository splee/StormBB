<%inherit file='/base.mak' />

<%def name='title()'>Login</%def>

<%def name='js()'>
function login() {
	var login_data = {
		username: $('#username').val(),
		password: $('#password').val()
	}

	$.post('/login', login_data, function(data) {
		if (data.status == 'ok') {
			window.location = "/";
		} else {
			var error = $('#error');
			error.text(data.msg);
			error.show();
		}
	});
}
// Prepare login form
$('#login').click(login);
$('#username').keydown(function(e) {if (e.keyCode == 13) $('#password').focus()});
$('#password').keydown(function(e) {if (e.keyCode == 13) login()});
$('#username').focus();
</%def>
<div id=error class="hidden error"></div>
<table>
<tr>
	<td><label for=username>Username</label></td>
	<td><input id=username></td>
</tr>
<tr>
	<td><label for=password>Password</label></td>
	<td><input id=password type=password></td>
</tr>
</table>
<input id=login type=button value=Login>
