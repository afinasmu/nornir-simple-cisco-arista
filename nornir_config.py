from nornir import InitNornir
from nornir.plugins.function.text import print_result
from nornir.plugins.tasks.networking import napalm_get

nr = InitNornir()

results = nr.run(
	task=napalm_get, getters=["facts","interface","environment","interfaces_ip"]
	)
	
print_result(results)