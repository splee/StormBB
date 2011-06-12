<%inherit file='/base.mak' />

<%def name='title()'>Index</%def>

% for cat in categories:
	<div class=category>
		<h3>${cat.name}</h3>
		% for board in cat.boards():
			<div class=board style="border: 1px solid black; margin: 2em;">
				<div class=title>
					<a href='/board/${str(board._id)}'>${board.name}</a>
					% if board.description:
					<p style="margin: 0; font-size: 0.8em;">${board.description}</p>
					% endif
				</div>
				<div class=stats>
					Topics: ${board.topic_count}<br/>
					Posts: ${board.post_count}
				</div>
			</div>
		% endfor
	</div>
% endfor
