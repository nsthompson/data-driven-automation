# data-driven automation

## Container Lab Setup

### vrnetlab

1. Clone vrnetlab repository

```shell
cd container-lab-topology
```

```shell
git clone https://github.com/hellt/vrnetlab.git
```

2. Copy and Prepare Cisco IOL images from Cisco CML refplat ISO

```shell
cp /Volumes/REFPLAT/virl-base-images/iol-xe-17-12-01/x86_64_crb_linux-adventerprisek9-ms ~/development/data-driven-automation-rh-summit-2025/container-lab-topology/vrnetlab/cisco/iol/cisco_iol-17.12.01.bin
```

```shell
cp /Volumes/REFPLAT/virl-base-images/ioll2-xe-17-12-01/x86_64_crb_linux_l2-adventerprisek9-ms ~/development/data-driven-automation-rh-summit-2025/container-lab-topology/vrnetlab/cisco/iol/cisco_iol-l2-17.12.01.bin
```

```shell
cd /workspaces/data-driven-automation-rh-summit-2025/container-lab-topology/vrnetlab/cisco/iol/
make docker-image
```
