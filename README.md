# mininet-basic-scripts
Software-defined network scripts written in Python using Mininet VM and Ryu SDN framework.
These scripts create several custom topologies running on a remote controller called Ryu.
<br>
<br>
Using Oracle VM VirtualBox and Ubuntu 20.04.2.0 LTS
<br>

Script | Description
------ | -----------
single.py | Custom single switch topology
linear.py | Custom linear topology
ring.py | Custom ring topology
run_cmds.py | Custom topology w/ running commands
link_changes.py | Custom topology w/ bringing down or up links

Run Ryu Controller on Ubuntu:
<br>
 `$ ryu-manager ryu.app.simple_switch_13`
<br>
 `$ ryu-manager ryu.app.simple_switch_stp # for ring topology`

 Run scripts on Ubuntu:
 <br>
 `$ sudo python <topology file name>`

 <br>
 
 [Link to Mininet Sample Workflow](http://mininet.org/sample-workflow/)
 <br>
 [Link to Mininet Walkthrough](http://mininet.org/walkthrough/)



