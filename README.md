#rubber

## Synopsis

This is a somewhat hacky script that wraps an http request in proxy protocol. I find it really useful for hitting health endpoints on servers that require proxy protocol.

## Usage

```
rubber <verb> <url> [options]
```

###positional arguments:
*  verb                  HTTP verb, Supported: GET, POST, PUT, and DELETE
*  url                   URL to send request to

###optional arguments:
*  -h, --help            Show this help message and exit
*  -s, --status-code     Return only the http response status code
*  --source SOURCE       Souce host for proxy
*  -p PORT, --port PORT  Destination port to communicate on
*  --dport DPORT         Source port for proxy
*  -d DATA, --data DATA  Data to send with the http request
*  -v, --verbose         Verbose output while making request
*  -n, --no-proxy        Send request without proxy protocol

#Installation
```

```
