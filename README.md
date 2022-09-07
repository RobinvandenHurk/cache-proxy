# Caching Proxy

The Caching Proxy is a Python-based lightweight proxy to support developers programming against rate-limited third-party
APIs. It's build to intercept all requests and respond with data from cache, or forward the request to the target host
if it hasn't seen this request yet.

![](media/usage.png)

### Usage

The proxy is extremely easy to use. Firstly, you spin up the proxy with `python proxy.py`. Then you just have to prepend
any request with `http://localhost/`.  

For example, if your original request is like this:
```shell
curl https://catfact.ninja/fact
```
Your new request would be like this:
```shell
curl http://localhost:5000/https://catfact.ninja/fact
```

### Installation
Installing this handy tool is about as easy as it gets:
```shell
git clone https://github.com/RobinvandenHurk/cache-proxy.git
pip install -r requirements.txt
```


### Why would you need this?

You may want to use this proxy if you are tasked with programming against a third-party API that applies rate-limiting.
During development you can easily send a bunch of requests which ultimately gets you (temporary) blocked, which may
drastically impact your productivity.

This simple proxy intercepts your requests and stores them in cache so that when you repeat the request, the proxy will
respond with the cached response rather than forwarding your request to the actual target host.

### What can you use this for?

This proxy was build to intercept API calls and respond from cache if possible. That means you can use it for most API
calls. However, it does not play nice with binary responses, like images. The primary focus of this proxy currently lies
in handling text based payloads, though binary support may be added later.

### TODO

* Improve cache strategies (Right now read from cache based on HTTP method and URL)