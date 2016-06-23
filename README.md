Rubber
======

This is a hacky script that wraps an http request in proxy protocol. I find it really useful for hitting health endpoints on servers that require proxy protocol.

Installation
------------

With `pip`

    pip install --upgrade git+git://github.com/quantumew/rubber.git

Without (install it in desired location)

    curl "https://raw.githubusercontent.com/quantumew/rubber/master/rubber" -o ./rubber
    chmod +x ./rubber


Usage
-----

    rubber <url> [options]

    URL                    - URL to send request to.
    -X VERB                - HTTP verb. defaults to GET, Supports: GET, POST, PUT, and DELETE.
    -s, --status-code      - Return only the http response status code.
    -d, --data DATA        - Data to send with HTTP request.
    -H, --headers HEADERS  - Headers to send with HTTP request. Supports multiple headers as separate strings. Ex. -H "Host: google.com" "Authorization: blah".
    -v, --verbose          - Outputs all content sent and received during the http request.
    -n, --no-proxy         - Send request without proxy protocol.
    -p, --port PORT        - Destination port to communicate on. This can alternatively be set with url, ie. "localhost:8080".
    --source SOURCE-HOST   - Souce host for proxy host info.
    --source-port PORT     - Source port for proxy host info.
    -h, --help             - Show script usage.

Examples
--------

Simple GET request that only returns the status code

    ./rubber https://test.com:8080/health --status-code

Example of a PUT request with header and data that isn't wrapped in proxy protocol

    ./rubber http://localhost:8080/artifact/hello-world -X PUT -H "Authorization: 190a64931e6e49ccb9917c7f32a29d19" -d '{"value": "val", "immutable": "false"}' --no-proxy
