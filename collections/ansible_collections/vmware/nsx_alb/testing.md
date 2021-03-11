# Testing Ansible Collection: vmware.nsx_alb

### Testing with `ansible-test`

install collection tar:

```
$ ansible-galaxy collection install vmware-nsx_alb-1.0.0.tar.gz
$ cd ~/.ansible/collections/ansible_collections/vmware/nsx_alb
```

```

Run `ansible-test`:

```
$ sudo ansible-test units --requirements -vvvv --docker
$ sudo ansible-test sanity --requirements -vvvv --docker
```

