TXC
===

Tux Containers - Make LXC easy for test-and-deploy

And Pegase is part of the adventure !

== Host Steps ==

1. Configure network interfaces (NAT, ip forwading, ...)

== Guest Steps ==

0. Load and create config for new machine
1. Generate builder from template (IP, iface, packages, ...)
2. Run image builder
3. Create user, add ssh authorized keys
4. Host: configure iptables, nginx

== Deployment steps ==

0. Make sure vm is stopped
1. Rsync vm (or zip)
2. Configure server
3. Launch on server
