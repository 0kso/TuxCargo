Tux Cargo
=========

Tux Containers - Make LXC easy for test-and-deploy

Introduction
------------

Linux Containers (LXC) are an awesome way to isolate processes
and create efficient and flexible virtual machines with Linux. 
Tux Cargo aims at building an easy way to configure and deploy
LXC virtual machines.

Main objectives are :
 * Creating new virtual machines with a NAT network configuration, the
   next IP available on your virtual network, your favourite packages, 
   your public ssh key and VIM settings, a preconfigured user, NGinx
   virtual hosts, iptables rules, ...
 * Deploying a virtual machine to a host and automatically reconfigure
   it for the new environment (network setup, NGinx virtual hosts, 
   iptables rules, ...)

<pre><code>
# txc create djangoblog
# ssh djangoblog.vm
(customizing machine...)
# txc deploy djangoblog host.superserver.net -h blog.mysite.net

# txc clone wordpressblog
(configuring machine...)
# txc deploy wordpressblog host.superserver.net -h otherblog.mysite.net 
</code></pre>

Host Steps
----------

1. Configure network interfaces (NAT, ip forwading, ...)

Guest Steps
----------

0. Load and create config for new machine
1. Generate builder from template (IP, iface, packages, ...)
2. Run image builder
3. Create user, add ssh authorized keys
4. Host: configure iptables, nginx

Deployment steps
----------------

0. Make sure vm is stopped
1. Rsync vm (or zip)
2. Configure server
3. Launch on server

* Pour info, je n'ai encore réussi qu'à créer correctement des conteneurs Debian (0kso)

(c) Copyright 2012 okso.me . Some Rights Reserved. 

This work is licensed under Free Software Foundation's 
<a rel="license" href="http://www.gnu.org/licenses/agpl-3.0.html">GNU AGPL v3.0</a>.

<a href="http://www.gnu.org/licenses/agpl-3.0.html">
    <img alt="AGPL Logo" src="http://www.gnu.org/graphics/agplv3-88x31.png" />
</a>