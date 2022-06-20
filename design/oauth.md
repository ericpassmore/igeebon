# Design for OAuth

## State Machine

The following states are kept on the client.
oauth token is stored on the client side. Client side storage is needed because the application is an extension of teamsnap and we don't need yet another authentication system. Client side allows simultaneous access.

| State | Description | Next State |
| ------ | ----------- | ---------- |
| init | start has token | authorized |
| init | start no token  | getting_token |
| init | unexpected response | error |
| get_code | redirect to 3rd party login succeed | create_token |
| get_code | unexpected response | error |
| create_token | create token and store token, succeed | authorized |
| create_token | bad or no token, failed | not_authorized |
| authorized | force reload page side effect remove token | init |
| authorized | expired token side effect remove token | init |
| authorized | unexpected response | error |
| not_authorized | hit retry/continue button | init |
| error | back to start | init |

### States

### init
- Input : nothing
- Service Calls : none

Checks for stored token and verifies non expired.

If valid token moves state to **authorized**

If no valid token moves state to **get_token** passes

If anything else client shows error. State moves to **error**.

### get_token
- Input : nothing
- Service Calls
  - local service get oauth metadata
  - authority URL with URL location to return to

client requests from server {authority=URL, redirect=URL}.
client sends user to redirect_url acquired initial request. user must log-in and authorize on third party.
redirect is returned with code appended to URL. client parses code. State moves to **create_token**

if redirect returns error or not authorized state moves to **error**.

*Note: can we tell if user was not authorized? if yes we can look into a non_authorized state transition*

### create_token
- Input : code
- Service Calls : authority generate token  

With code client creates an HTTPS call to the generate the token. If success state moves to **authorized**. If call fails state moves to **not_authorized**.

If error encountered then state is **error**.

### authorized
- Input : nothing
- Service Calls : none

This is a final state, with client storing auth token, all work is done.

### not_authorized
- Input : nothing
- Service Calls : none

This is a final state, with client not storing auth token, or holding an invalid token

### error
- Input : error message
- Service Calls: none

something unexpected happened. shows error message to user
