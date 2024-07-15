
**Web-version [here](https://palmaitem.github.io/kgcompliance/)**

# Using Knowledge Graphs to Automate Network Compliance of Containerized Services

## Abstract

Information and Communication Technology (ICT) infrastructures are increasingly adopting software-based approaches, using paradigms such as Infrastructure as Code (IaC).  
This is aligned with the design of modern systems, such as 5G with the use of Virtual Network Functions (VNFs) and containerized services, combining the expertise and participation of various stakeholders from diverse cultural and educational backgrounds, potentially across different organizations. 
Such organizations depend on efficient knowledge management to overcome the interoperability challenges arising from both technical and organizational complexity. 
To create a common understanding of containerized networking infrastructures, we developed an ontology that allows a unified representation of core networking concepts. 
By enriching pre-deployment tasks with semantics, we universally represented and verified different network policies based on formal logic. 
To validate our approach, we constructed two knowledge graphs using open-source 5G Core Network implementations and demonstrated the potential of our approach by checking for compliance with automated reasoning. 
Using our defined rules, we extracted knowledge about non-compliant services and made inferences based on the well-defined concepts in the ontology. 
Our findings suggest that different network security policies can be integrated into each knowledge base, contributing to autonomic and cognitive management of future infrastructures. 
This can potentially provide more reliable IaC definitions, improve machine interpretation of IaC deployments, and assist human actors in making better-informed decisions.

## Results overview

This page presents the resulting Knowledge Graphs (KGs) for:

- [Free5GC](Free5GC-KB/KGraph4.html){:target="_blank"} with the populated knowledge base derived from [Free5GC repository](https://github.com/free5gc/free5gc-compose/blob/d04baa57a6e4c9a2c4af8a223bad984299d100b7/docker-compose.yaml).
- [OAI5GC](OAI5GC-KB/KGraph5.html){:target="_blank" rel="noopener"} with the populated knowledge base derived from the [OAI Basic 5G repository](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-fed/-/blob/94ecfac7476114f730e1b555779a20b3e78d77f0/docker-compose/docker-compose-basic-nrf.yaml).

These KGs are **interactive** and allow exploring all the implicit knowledge that exists in typical Infrastructure as Code setups, and which is made explicit.
With our approach we can apply mathematical logic and automated reasoning to define compliance rules and verify them.

## More results

A repository containing all the relevant data and parsing code is available on [github](https://github.com/aleksandra-simic/TTM4905).


## Contact details 

This project has been created by Aleksandra Simić, under the supervision of David Palma.

- Email: aleksandra.simic@ntnu.no
- Email: david.palma@ntnu.no
