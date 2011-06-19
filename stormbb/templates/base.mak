<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, minimum-scale=1.0, maximum-scale=1.0" />
	
	<title>${self.title()} - Tempest Forums</title>
	
	<!-- The framework -->
	<link rel="stylesheet" href="/static/css/inuit.css" />
	<link rel="stylesheet" href="/static/css/breadcrumb.inuit.css" />
	
	<style>
		.hidden {
			display: none;
		}
		.error {
			font-color: red;
		}
		.headbar {
			padding: 5px;
			background: #eee;
			border-bottom: 1px solid black;
			font-size: 1.3em;
			margin-bottom: 5px;
			text-align: center;
		}
	</style>
</head> 
</head>
<body>
<div class="headbar">This is currently read only. To talk to real people,
<a href="http://convore.com/tempest/">head over to Convore</a>.</div>
	
	<!-- YOU CAN START WORKING IN THIS FILE RIGHT AWAY, JUST EDIT BELOW -->
	<div class="grids">
	
		<div id="side" class="grid-4">
			<h1><a href="/">Tempest PA</a></h1>
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
		<div id="page" class="grid-12">
			
			${next.body()}
			
		</div>
	</div>
	
</body>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js">
</script>
<script>
	${self.js()}
</script>
</html>\

<%def name='title()'>Home</%def>\
<%def name='js()'></%def>\

