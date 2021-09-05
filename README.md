# rydja-client

This is a basic implementation of a ryðja client in Python.

## Running the client

In the root directory, run `python3 src/main.py` to interact with the client.

## Current functionality

There are many, many limitations to the current implementation of this client (as of 5 September 2021):
* Cannot handle in-line tags (`@i`, `@b`, `@u`, `@link`, etc.)
* Can only query a server running on localhost
* Cannot handle other domains
* Cannot interact with the page in the terminal (no scrolling or tabbing through links)

These features will be added in accordance with the project board.
