<%inherit file='/base.mako' />

<%def name='title()'>${board.name}</%def>

<ol class="breadcrumb">
	<li><a href="/">Boards</a></li>
	<li>${board.name}</li>
</ol>
<p class=meta>${board.description}</p>
<table>
	<tr>
		<th>Title</th>
		<th>Replies</th>
		<th>Last Update</th>
		<th>Sticky</th>
	</tr>
	% for topic in board.topics():
	<tr>
		<td><a href="/topic/${str(topic._id)}">${topic.title}</a></td>
		<td>${topic.reply_count}</td>
		<td>${topic.last_update}</td>
		<td>${topic.is_sticky}</td>
	</tr>
	% endfor
</table>
