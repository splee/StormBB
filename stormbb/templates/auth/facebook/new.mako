<%inherit file='/base.mako' />

<%def name='title()'>Welcome, ${c.profile['first_name']}!</%def>

<h2>Welcome to the Tempest forums!</h2>

<p>Please choose a user name.  It must be unique and it should be awesome. No pressure.</p>

% if hasattr(c, 'error'):
    <p class="error">${c.error}</p>
% endif

<h3>New Users</h3>
<form id='choose_username' action='/auth/facebook/new' method='POST'>
    <label for="username">User name</label>
    <input id="username" name="username" type='text' placeholder='Enter user name here' />
    <input type='submit' value='Create user' />
</form>
<br/>

<h3>Existing Users</h3>
<form id="existing_user" action="/auth/facebook/existing" method="POST">
    <label for="username">Existing user name</label>
    <input id="eusername" name="username" type="text" placeholder="Existing user name" />

    <label for="password">Password</label>
    <input id="password" name="password" type="password" />

    <input type='submit' value='Claim existing account' />
</form>
