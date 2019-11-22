#!/usr/bin/env python3.7

import subprocess


docker_ps_a = "docker ps -a"
process = subprocess.Popen(docker_ps_a.split(), stdout=subprocess.PIPE, text=True)
output, error = process.communicate()


docker_cont_names = [] # list of all docker container names
for line in output.splitlines()[1:]:
    docker_cont_names.append(line.split()[-1])


docker_volume_ls = "docker volume ls"
process = subprocess.Popen(docker_volume_ls.split(), stdout=subprocess.PIPE, text=True)
output, error = process.communicate()


docker_volume_names = [] # list of all docker volume names
for line in output.splitlines()[1:]:
    docker_volume_names.append(line.split()[-1])


for docker_container in docker_cont_names:
    for volume_name in docker_volume_names:
        docker_cmd = f'docker container inspect {docker_container} | grep {volume_name}'
        process = subprocess.Popen(docker_cmd, stdout=subprocess.PIPE, shell=True, text=True)
        output, _ = process.communicate()
        if output != '':
            print(docker_container, '-->', output)
