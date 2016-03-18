#rubber

## Synopsis

This is a somewhat hacky script that wraps an http request in proxy protocol. I find it really useful for hitting health endpoints on servers that require proxy protocol.

## Usage

```
rubber <verb> <url> [options]
```

###Example

```
rubber GET http://test.com:8080/health --status-code
```

###positional arguments:
*  VERB
    * HTTP verb, Supported: GET, POST, PUT, and DELETE
*  URL
    * URL to send request to

###optional arguments:
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
