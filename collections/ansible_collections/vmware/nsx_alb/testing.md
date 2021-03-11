# Testing Ansible Collection: vmware.nsx_alb

### Testing with `ansible-test`

##### Install collection tar

```
$ ansible-galaxy collection install vmware-nsx_alb-1.0.0.tar.gz
$ cd ~/.ansible/collections/ansible_collections/vmware/nsx_alb
```
##### Run ansible tests

```
$ sudo ansible-test units --requirements -vvvv --docker
$ sudo ansible-test sanity --requirements -vvvv --docker
