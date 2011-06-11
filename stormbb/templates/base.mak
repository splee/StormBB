<!doctype html>
<html>
<head>
	<title>${self.title()} - Tempest Forums</title>
	<style>
		.hidden {
			display: none;
		}
		.error {
			font-color: red;
		}
	</style>
</head>
<body>
<div id=header>
% if USER_ID:
	<p>
		Welcome back, ${USER_DISPLAY_NAME}!
		<a href="/logout">Log Out</a>
	</p>
% else:
	<p>
		Welcome to the forums.
		<a href="/login">Log In</a>
	</p>
% endif
</div>
${next.body()}
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js">
</script>
<script>
	${self.js()}
</script>
</body>
</html>\

<%def name='title()'>Home</%def>\
<%def name='js()'></%def>\

