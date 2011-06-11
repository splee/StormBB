
<%inherit file='/base.mak' />

<%def name='title()'>Index</%def>

% for cat in categories:
	<div class=category>
		<h3>${cat.name}</h3>
		% for board in cat.boards():
			<div class=board>
			<a href='/board/${str(board._id)}'>${board.name}</a>
			</div>
		% endfor
	</div>
% endfor
