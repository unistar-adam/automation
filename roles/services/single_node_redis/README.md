Role Name
=========
.
├── ansible.cfg
├── inventory
│   └── Home_container
├── playbook
│   └── service
│       └── single_node_redis.yaml
├── roles
│   └── services
│       └── single_node_redis
│           ├── README.md
│           ├── defaults
│           │   └── main.yml
│           ├── files
│           │   └── redis.service
│           ├── handlers
│           │   └── main.yml
│           ├── meta
│           │   └── main.yml
│           ├── tasks
│           │   ├── common
│           │   │   ├── Configuration_redis_into_systemd.yaml
│           │   │   ├── Install_redis.yaml
│           │   │   └── Verify_redis.yaml
│           │   └── main.yml
│           ├── tests
│           │   ├── inventory
│           │   └── test.yml
│           └── vars
│               └── main.yml
└── utility.code-workspace

Requirements
------------
OS: CentOS 7.X by systemd

Dependencies
------------
packages:
 - gcc
 - make
 - which
 - redis-5.0.5

verify_packages:
 - tcl

Service Account
redis/redis UID:996 GID:996

Example Playbook
----------------

ansible-playbook -e "hostname={host}" playbook/service/single_node_redis.yaml

Author Information
------------------

Shang-Kuan, Chen

Update history
------------------

2019/06/18
  Init by redis-5.0.5