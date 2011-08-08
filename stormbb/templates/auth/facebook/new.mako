<%inherit file='/base.mako' />

<%def name='title()'>Welcome, ${first_name}!</%def>

<h2>Welcome to the Tempest forums!</h2>

<p>Please choose a user name.  It must be unique and it should be awesome. No pressure.</p>

<form id='choose_username' action='/auth/facebook/new' method='POST'>
    <label for="username">User name:</label>
    <input type='text' placeholder='Enter user name here' />
    <input type='submit' value='Create user' />
</form>
