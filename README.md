# python-hover-client

A simple python library for managing domains registered at hover.com.

### Credits

This project is [based](http://gist.github.com/jmckind/7763461) primarily on the original [gist](http://gist.github.com/dankrause/5585907) by [Dan Krause](http://gist.github.com/dankrause), with [updates](http://gist.github.com/rleemorlang/7225451) by [Rick Lee-Morlang](http://gist.github.com/rleemorlang).

### Usage

First, authenticate using Hover account credentials.

	from hover import *

    client = HoverAPI("myusername", "mypassword")

Get domain details without DNS records

	client.call("get", "domains")

Get all domains and DNS records

	client.call("get", "dns")

Specify an "id" (from the list calls above) to address the domains individually.

Get the details for a specific domain without DNS records

	client.call("get", "domains/dom123456")

Get DNS records for a specific domain

	client.call("get", "domains/dom123456/dns")

Create a new A record

	record = {"name": "mysubdomain", "type": "A", "content": "127.0.0.1"}
	client.call("post", "domains/dom123456/dns", record)

Create a new SRV record
Content is "{priority} {weight} {port} {target}"

	record = {"name": "mysubdomain", "type": "SRV", "content": "10 10 123 __service"}
	client.call("post", "domains/dom123456/dns", record)

Create a new MX record
Content is "{priority} {host}"

    record = {"name": "mysubdomain", "type": "MX", "content": "10 mail"}
	client.call("post", "domains/dom123456/dns", record)

Update an existing DNS record

    client.call("put", "dns/dns1234567", {"content": "127.0.0.1"})

Delete a DNS record:

    client.call("delete", "dns/dns1234567")
