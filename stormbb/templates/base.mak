<!doctype html>
<html>
<head>
	<title>%{self.title()} - Tempest Forums</title>
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

