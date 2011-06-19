<%inherit file='/base.mak' />

<%def name='title()'>${topic.title}</%def>

<ol class="breadcrumb">
	<li><a href="/">Boards</a></li>
	<li><a href="/board/${str(topic.board._id)}">${topic.board.name}</a></li>
	<li>${topic.title}</li>
</ol>

<table>
	<tr>
		<th>Author</th>
		<th>Message</th>
	</tr>
	% for message in topic.messages():
	<tr>
		<td>
		% if message.author:
			${message.author.display_name}
		% else:
			Unknown
		% endif
		</td>
		<td>${message.rendered_body}</td>
	</tr>
	% endfor
</table>
