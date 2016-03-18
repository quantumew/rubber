#rubber

## Synopsis

This is a somewhat hacky script that wraps an http request in proxy protocol. I find it really useful for hitting health endpoints on servers that require proxy protocol.

## Usage

```
rubber <verb> <url> [options]
```

###Examples

* Simple GET request that only returns the status code
    * `./rubber http://test.com:8080/health --status-code`

* Example of a PUT request with header and data that isn't wrapped in proxy protocol
    * `./rubber http://localhost:8080/artifact/hello-world -X PUT -H "Authorization: 190a64931e6e49ccb9917c7f32a29d19" -d '{"value": "val", "immutable": "false"}' --no-proxy`

###positional arguments:
*  URL
    * URL to send request to

###optional arguments:
* HTTP verb, Supported: GET, POST, PUT, and DELETE
    * -X VERB
*  Show help message and exit
    * -h | --help
* Return only the http response status code
    * -s, --status-code
* Souce host for proxy
    * --source SOURCE-HOST
* Destination port to communicate on. This can alternatively be set with url, ie. localhost:8080
    * -p | --port PORT
* Source port for proxy.
    * --source-port PORT
* Data to send with HTTP request.
    * -d | --data DATA
* Headers to send with HTTP request. Currently doesn't support multiple (like curl). Requires /r/n characters.
    * -H | --headers HEADERS
* Verbose output while making request
    * -v | --verbose
* Send request without proxy protocol. WHY ARE YOU EVEN USING THIS SCRIPT LOL!!
    * -n | --no-proxy
