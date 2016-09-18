# dockswarmbeat
Docker heartbeat for swarm, sending info to gelf Logstash

Run with:
```
docker service create << ADD MOUNT >> -v /var/run/docker.sock:/var/run/docker.sock --log-driver=gelf --log-opt gelf-address=udp://<logstash IP>:12201 --name dockswarmbeat  djbnjack/dockswarmbeat
```
