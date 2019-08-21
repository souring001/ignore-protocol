# ignore-protocol
This protocol never minds loss packets.

## get started
Set your ip address and port in `robust_client.py`, `robust_server.py` as follows:

```python
ip_dst = '192.168.12.101'
ip_src = '192.168.12.102'
port = 2525
```

Make directory `checkFiles/src`, `checkFiles/dst` and insert files into `checkFiles/src` directory.

## run

Mode: send

```bash
python robust_client.py
python robust_server.py
```

or

```bash
python robust_client.py 0
python robust_server.py 0
```

Mode: Receive
```bash
python robust_client.py 1
python robust_server.py 1
```
