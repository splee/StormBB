<%inherit file='/base.mak' />

<%def name='title()'>User Admin</%def>

<table>
<thead>
	<tr>
		<th>Username</th>
		<th>Display Name</th>
		<th>Groups</th>
	</tr>
</thead>
<tbody>
	% for user in users:
	<tr>
		<td>${user.username}</td>
		<td>${user.display_name}</td>
		<td>${', '.join(user.groups)}</td>
	</tr>
	% endfor
</tbody>
</table>
