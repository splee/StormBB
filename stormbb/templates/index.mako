<%inherit file='/base.mak' />

<%def name='title()'>Index</%def>

<ol class="breadcrumb">
	<li>Boards</li>
</ol>

<table>
	% for cat in categories:
		<thead>
			<tr>
				<th colspan="2">${cat.name}</th>
			</tr>
		</thead>
		<tbody>
		% for board in cat.boards():
			<tr>
				<td>
					<a href='/board/${str(board._id)}'>${board.name}</a>
				</td>
				<td>
					${board.topic_count} topics
				</td>
			</tr>
		% endfor
		</tbody>
	% endfor
</table>
