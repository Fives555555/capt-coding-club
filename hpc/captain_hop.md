Edit your ssh config file in
```
~/.ssh/config
```
(you may need to create the config file)

then add the following lines replacing with you username:
```
Host captain
     hostname captain
     user <your_username>

Host ada
     hostname hpclogin01.ada.nottingham.ac.uk
     user <your_username>
     proxyjump captain
```
Now you should be able to connect using:

```
ssh ada
```

Alternatively, if you have a static ip address, you can submit a firewall exception request via https://selfservice.nottingham.ac.uk.
