<%inherit file='/base.mak' />

<%def name='title()'>${topic.title}</%def>

<h3>${topic.title}</h3>

<div class="messages">
% for message in topic.messages():
	<div class=message style="margin: 1em; padding: 5px;">
ID: ${message.id}
		% if message.author:
			<p class=meta>Author: ${message.author.display_name}</p>
		% else:
			<p class=meta>Author: Unknown</p>
		% endif
		<div class=message-body>${message.rendered_body}</div>
	</div>
% endfor
</div>
