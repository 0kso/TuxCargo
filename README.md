TXC
===

Tux Containers - Make LXC easy for test-and-deploy

And Pegase is part of the adventure !
Thanks to 0kso, I can join :DDDD

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

* Pour info, je n'ai encore réussi qu'à créer correctement des conteneurs Debian (0kso)

(c) Copyright 2012 okso.me . Some Rights Reserved. 

This work is licensed under Free Software Foundation's 
<a rel="license" href="http://www.gnu.org/licenses/agpl-3.0.html">GNU AGPL v3.0</a>.