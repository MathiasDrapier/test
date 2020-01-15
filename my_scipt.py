                
import docker
import subprocess

client=docker.from_env()

bashCommand = """head -1 /proc/self/cgroup|cut -d/ -f3"""
output = subprocess.check_output(['bash','-c', bashCommand])
con_id=output[0:12]
con_id_str=con_id.decode("utf-8")
print(con_id_str)
container=client.containers.get(con_id_str)
print(container.stats(stream=False))
