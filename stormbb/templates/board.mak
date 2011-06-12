<%inherit file='/base.mak' />

<%def name='title()'>${board.name}</%def>

<h3>${board.name}</h3>
<p class=meta>${board.description}</p>

<div class="topics">
% for topic in board.topics():
	<div class=topic style="margin: 1em; padding: 5px;">
		<a href="/topic/${str(topic._id)}">${topic.title}</a>
		<div>Replies: ${topic.reply_count}</div>
		<div>Last Update: ${topic.last_update}</div>
		<div>Sticky: ${topic.is_sticky}</div>
	</div>
% endfor
</div>
