Implementing Service Oriented Architecture (SOA) using HTTP is a horrible idea
##############################################################################

:date: 2014-11-16
:tags: programming, infrastructure
:category: Programming
:authors: Kushagra Sinha


`Service Oriented Architecture <http://en.wikipedia.org/wiki/Service-oriented_architecture>`_
is a commonly used design pattern in distributed and enterprise applications.
It involves the creation and use of independent *services* that work together
to produce the desired result. The most important benefits, of course, are
separation of concerns and the ability to scale each service independent of
others, leading to a clean, modular design.

A common problem faced during the design of a SOA system is the choice of
communication protocol. Ideally we want our services to communicate with each
other with minimum communication overhead. This involves:

* Low latency
* High throughput

Many open source protocols are available for use in SOA. Some of them also
provide client/server de-serialization/serialization libraries to make your job
easier. Examples are:

* `Protocol Buffers <https://developers.google.com/protocol-buffers/>`_
* `Apache Thrift <https://thrift.apache.org/>`_
* `Apache Avro <http://avro.apache.org/>`_

Some people also like to use SOAP, XML-RPC, JSON-RPC etc. I have attempted to
cover the (mis)use of HTTP/REST as a SOA protocol in this article.

Consider 2 clients accessing a web front-end for some data. The web frontend
server is responsible for some preprocessing (authentication etc.) and
post-processing (aggregation etc.) tasks. The heavy lifting is done by our
backend service.

|SOA-Image|

.. |SOA-Image| image:: {filename}/images/soa.png

Let us say Client1 came first and requested for Data1. The web frontend
performs some preprocessing on the request and forwards it to our backend
service over HTTP. Meanwhile Client2 came along and requested for Data2. Now,
if our backend service has not yet returned with Client1's request, the web
frontend cannot effectively re-use (multiplex) the TCP connection between
itself and our backend service since the HTTP protocol requires servers to
return responses in the same order as requests. Our web frontend will need to
create a new TCP connection for each concurrent request which is extremely
wasteful. `SPDY <http://www.chromium.org/spdy/spdy-protocol/spdy-protocol-draft2>`_
has tried to address the multiplexing issue but it may be a bit away from
production grade quality yet.

Another problem is HTTP/1.1's use of ASCII. Sure it makes things easier to
debug but again is wasteful in SOA. Ideally we want a tightly packed binary
protocol.

HTTP/1.1's statelessness is another cause of worries. It is simply wasteful
to send the same set of headers for similar requests. Again, SPDY and HTTP/2.0
are trying header compression and may be worth
`looking into <http://chimera.labs.oreilly.com/books/1230000000545/ch12.html#HTTP2_HEADER_COMPRESSION>`_.

Conclusion
==========

HTTP/1.1 is an excellent protocol for a traditional client/server model. It is
an ASCII protocol, hence it is easy to debug. It is fairly well known, has a
number of supporting libraries in almost all major languages and provides a
useful set of primitives and verbs for almost all of your data transfer needs.
However, please do not use it if you are creating a production grade SOA
application.
