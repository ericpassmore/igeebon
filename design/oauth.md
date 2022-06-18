# Design for OAuth

## State Machine

The following states are kept on the client.
oauth token is stored on the server side, and never exposed to the client.


| State | Description | Next State |
| ------ | ----------- | ---------- |
| init | start has token | authorized |
| init | start no token  | getting_token |
| init | unexpected response | error |
| get_code | redirect to 3rd party login succeed | create_token |
| get_code | unexpected response | error |
| create_token | server side create token succeed | authorized |
| create_token | server side token failed | not_authorized |
| authorized | force reload page side effect remove token | init |
| authorized | expired token side effect remove token | init |
| authorized | unexpected response | error |
| not_authorized | hit retry/continue button | init |
| error | back to start | init |

### States

### init

Server checks for token and verifies non expired.

If valid token, then server returns 200 OK, with body of {valid_oauth_token}. client parses response and moves state to **authorized**

If no valid token, then server returns 200 OK, with body of {no_oauth_token, authority=URL, redirect=URL}. client parses response , moves state to **get_token** passes on authority and redirect

If anything else client shows error "Invalid Response Returned Code XXX". State moves to **error**.

### get_token

client sends user to redirect_url acquired initial request. user must log-in and authorize on third party.
redirect is returned with code appended to URL. client parses code. State moves to **create_token**

if redirect returns error or not authorized state moves to **error**.

*Note: can we tell if user was not authorized? if yes we can look into a non_authorized state transition*

### create_token

With code from authorization provide execute service side call the generate the token. If success state moves to **authorized**. If call fails state moves to **not_authorized**.

If error encountered then state is **error**.

### authorized

This is a final state, with server storing the auth token required for access.

### not_authorized

This is a final state, with server not storing auth token, or holding an invalid token

### error

something unexpected happened. shows error message to user
