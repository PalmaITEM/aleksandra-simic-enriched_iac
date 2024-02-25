import yaml
import os
import owlready2


###Functions for parsing and populating the ontology with information from docker-compose.yaml file###

#loading docker compose file and storing in python dictionary
def load_docker_compose():
    directory = 'public repo/OAI5GC-KB' #add your path to the directory
    docker_compose_files = []
    for file in os.listdir(directory):
        if file.endswith(".yaml") or file.endswith(".yml"):
            docker_compose_files.append(os.path.join(directory, file))
    docker_compose_dict = {}
    for file in docker_compose_files:
        with open(file, 'r') as f:
            docker_compose_dict[os.path.basename(f.name)] = yaml.safe_load(f)
    return docker_compose_dict

#printing docker compose file
def print_docker_compose():
    for key in load_docker_compose():
        print(key)
        for key2 in load_docker_compose()[key]:
            print(key2, '->', load_docker_compose()[key][key2])
            if isinstance(load_docker_compose()[key][key2], dict):
                for key3 in load_docker_compose()[key][key2]:
                    print(key3, '->', load_docker_compose()[key][key2][key3])



#extracting the name of the application from the compose file name
#adjust app_name based on the name of the file                    
def extract_name(compose_file):
    if 'yaml' in compose_file:
        compose_name = compose_file.split('.yaml')[0]
        #app_name=compose_name.split('compose')[0] #for apps
        #for 5gc cases
        app_name=compose_name.split('docker-compose')[0]
    elif 'yml' in compose_file:
        compose_name = compose_file.split('.yml')[0]
        #app_name=compose_name.split('compose')[0] #for apps
        #for 5gc cases
        app_name=compose_name.split('docker-compose')[0]
    return app_name    


#listing all the values for services in docker_d dictionary
def list_services_networks(docker_d):
    services = []
    networks = []
    for key in docker_d:
        app_name = extract_name(key)
        for key2 in docker_d[key]:
            if key2 == 'services':
                for key3 in docker_d[key][key2]:
                    service=app_name+key3
                    services.append(service)
            if key2 =='networks':
                for key3 in docker_d[key][key2]:
                    network=app_name+key3
                    networks.append(network)
    return services, networks

#populating ontology with services and networks
def populate_ontology_with_services_and_networks(services,networks):
    for i in range(0, len(services)):
        onto.Service(services[i])  
    for i in range(0, len(networks)):
        network.IPNetwork(networks[i])
    


#populating the ontology with services and respective networks from the dictionary using hasIPnetwork object property      
def populate_with_services_hasIPNetwork_network(docker_d):
    for key in docker_d:
        app_name = extract_name(key)
        for key2 in docker_d[key]:
            if key2 == 'services':
                for key3 in docker_d[key][key2]:
                    for key4 in docker_d[key][key2][key3]:
                        if key4 == 'networks':
                            for key5 in docker_d[key][key2][key3][key4]:
                               service=app_name+key3
                               network_name=app_name+key5
                               onto.Service(service).hasIPNetwork.append(network.IPNetwork(network_name))



#extracting defined subnets and the respective network from the dictionary
def extract_subnets(docker_d):
    subnets = []
    for key in docker_d:
        app_name = extract_name(key)
        for key2 in docker_d[key]:
            if key2 == 'networks':
                for key3 in docker_d[key][key2]:
                    if docker_d[key][key2][key3] is not None:
                        for key4 in docker_d[key][key2][key3]:
                            if key4 == 'ipam':
                                for key5 in docker_d[key][key2][key3][key4]:
                                    if key5 == 'config':
                                        subnet_name = app_name+key3
                                        subnets.append(subnet_name)
                                        for key6 in docker_d[key][key2][key3][key4][key5]:
                                            subnets.append(key6.get('subnet',''))                       

    return subnets


#populating ontology with respective subnets for each network using hasSubnet data type property
def populate_ontology_with_subnets(subnets,networks):
    for i in range(0, len(subnets)):
        if subnets[i] in networks: 
            j=i+1
            while j < len(subnets):
                if '/' in subnets[j]:
                    network.IPNetwork(subnets[i]).hasSubnet.append(subnets[j])
                    j+=1
                else:
                    break



#extracting ipv4 and ipv6 from the dictionary. 
#storing information as a dictionary, example: {service1:{network1: {ipv4:'ip address', ipv6:'ip address'}}}
#populating the ontology with IP addresses (hasStaticIP, ipAddressVersion, hasIPAddressValue and belongsToIPNetwork properties)
def extract_and_populate_ip_addresses(docker_d):
    static_ipv4 = {}
    static_ipv6 = {}
    for key in docker_d:
        app_name = extract_name(key)
        for key2 in docker_d[key]:
            if key2 == 'services':
                for key3 in docker_d[key][key2]:
                    for key4 in docker_d[key][key2][key3]:
                        if key4 == 'networks':
                            if isinstance(docker_d[key][key2][key3][key4], dict):
                                for key5 in docker_d[key][key2][key3][key4]:
                                    for key6 in docker_d[key][key2][key3][key4][key5]:
                                        service_name=app_name+key3
                                        network_name=app_name+key5
                                        if key6 == 'ipv4_address':
                                            static_ipv4[key3] = {}
                                            static_ipv4[key3][key5] = {}
                                            static_ipv4[key3][key5]['ipv4'] = docker_d[key][key2][key3][key4][key5][key6]
                                            network.IPAddress(docker_d[key][key2][key3][key4][key5][key6])
                                            onto.Service(service_name).hasStaticIP.append(network.IPAddress(docker_d[key][key2][key3][key4][key5][key6]))
                                            network.IPAddress(docker_d[key][key2][key3][key4][key5][key6]).ipAddressVersion.append('4')
                                            network.IPAddress(docker_d[key][key2][key3][key4][key5][key6]).hasIPAddressValue.append(docker_d[key][key2][key3][key4][key5][key6])
                                            network.IPAddress(docker_d[key][key2][key3][key4][key5][key6]).belongsToIPNetwork.append(network.IPNetwork(network_name))
                                        if key6 == 'ipv6_address':
                                            static_ipv6[key3] = {}
                                            static_ipv6[key3][key5] = {}
                                            static_ipv6[key3][key5]['ipv6'] = docker_d[key][key2][key3][key4][key5][key6]
                                            network.IPAddress(docker_d[key][key2][key3][key4][key5][key6])
                                            onto.Service(service_name).hasStaticIP.append(network.IPAddress(docker_d[key][key2][key3][key4][key5][key6]))
                                            network.IPAddress(docker_d[key][key2][key3][key4][key5][key6]).ipAddressVersion.append('6')
                                            network.IPAddress(docker_d[key][key2][key3][key4][key5][key6]).hasIPAddressValue.append(docker_d[key][key2][key3][key4][key5][key6])
                                            network.IPAddress(docker_d[key][key2][key3][key4][key5][key6]).belongsToIPNetwork.append(network.IPNetwork(network_name))
                                        
    return static_ipv4, static_ipv6


#extracting ports from dictionary and populating ontology using the exposesPortToHost and exposesPortToServices data type properties
def extract_populate_ports(docker_d):
    ports = {}
    for key in docker_d:
        app_name = extract_name(key)
        for key2 in docker_d[key]:
            if key2 == 'services':
                for key3 in docker_d[key][key2]:
                    for key4 in docker_d[key][key2][key3]:
                        service_name = app_name+key3
                        if key4 == 'ports':
                            for i in docker_d[key][key2][key3][key4]:
                                if ":" in i:
                                    container_port = i.split(':')[1]
                                    if service_name not in ports:
                                        ports[service_name] = []
                                    ports[service_name].append(container_port)
                                    onto.Service(service_name).exposesPortToHost.append(container_port)
                                else:
                                    container_port=i['target']
                                    if service_name not in ports:   
                                        ports[service_name] = []
                                    ports[service_name].append(container_port)
                                    onto.Service(service_name).exposesPortToHost.append(container_port)
                        if key4 == 'expose':
                            for i in docker_d[key][key2][key3][key4]:
                                if service_name not in ports:
                                    ports[service_name] = []
                                ports[service_name].append(i)
                                #port value is a string in the ontology
                                if isinstance(i,int):
                                    i = str(i)
                                onto.Service(service_name).exposesPortToServices.append(i)
    return ports





###Utilizing functions for data processing tasks###


#load compose files and store in dictionary
docker_d=load_docker_compose()

#load ontology
onto = owlready2.get_ontology('public repo/Container-Networking-Ontology/Ontology-extended.rdf').load() #add your path to the ontology with the .rdf extension

#get namespace of the imported ontology (Network Infrastructure Ontology)
network=onto.get_namespace("http://w3id.org/devops-infra/network#")


#extract services and networks and populate the knowledge base
services, networks = list_services_networks(docker_d)


#populate ontology with services and networks
populate_ontology_with_services_and_networks(services,networks)


#populate the ontology with custom networks
populate_with_services_hasIPNetwork_network(docker_d)


#print all the services and their networks 
print("After populating with hasIPNetwork")
for key in onto.Service.instances():
    print(key.name, '->', key.hasIPNetwork)


#extract and populate static IP addresses
static_ipv4,static_ipv6 = extract_and_populate_ip_addresses(docker_d)


#print all the services and their static IP addresses
for key in onto.Service.instances():
    print(key.name, '->', key.hasStaticIP)



#extract subnets from docker_d dictionary
subnets=extract_subnets(docker_d)


#populate ontology with subnets
populate_ontology_with_subnets(subnets,networks)


#extract and populate ontologies with ports
extract_populate_ports(docker_d)


#print all the services and the exposed ports
for key in onto.Service.instances():
    print(key.name, '->', key.exposesPortToHost)
    print(key.name, '->', key.exposesPortToServices)



#different individuals of a class Service
for key in onto.Service.instances():
    for key2 in onto.Service.instances():
       if key.name != key2.name:
            owlready2.AllDifferent([key,key2])


#different indviduals of a class IPNetwork
for key in network.IPNetwork.instances():
    for key2 in network.IPNetwork.instances():
       if key != key2:
            owlready2.AllDifferent([key,key2])



onto.save(file = "public repo/OAI5GC-KB/KB5.owl", format = "rdfxml")  #add your path to the populated ontology with the .owl extension


#This script has been generated with the assistance of the GitHub Copilot. 