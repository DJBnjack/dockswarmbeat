# dockswarmbeat
Docker heartbeat for swarm, sending info to Elasticsearch (ad-hoc!)

Run with:
```
docker run -it --rm -v /var/run/docker.sock:/var/run/docker.sock DJBnjack/dockswarmbeat python app.py <ip-of-ES-host>
```
