# TTM4905 - Master's Thesis

## Speaking the Same Language Through Logic and Ontologies

### Short description
Throughout this thesis, we explored the Semantic Web Technologies and Description Logics to represent core networking aspects of the infrastructure defined as code. 
For that, the Container Networking Ontology has been created based on the definition of Docker services and networks within `compose.yaml` files. 
Moreover, we designed the Data Parsing and Populating Module for populating the ontology with data from publicly available projects, demonstrating the analysis of different scenarios.

## Project overview
This repository contains the supplementary material for this master's thesis. 
It consists of the Container Networking Ontology in RDF/XML and Turtle formats, in two versions, with and without properties defined for integration of SWRL rules.
Knowledge bases for each use case are also available in two formats: populated ontology with data from Docker Compose files (1) and extended knowledge base with SWRL rules (2). 
Knowledge graphs are available in HTML format, while it is recommended to open them in any of the browsers for interactive navigation and detail inspection. 


## Project structure
This repository is organized as follows:

- The foundational and extended version with properties for verifying rules can be found at [Container Networking Ontology](Container-Networking-Ontology/). 

- The knowledge bases built based on the [Awesome Docker Compose samples](https://github.com/docker/awesome-compose), multi integrated services, according to the naming used in the thesis, are:
    - [All 21](All-21-KB/) with the populated knowledge base, extended with SWRL rules and knowledge graph files. 
    - [App 1](App-1-KB/) with the populated knowledge base, extended with SWRL rules and knowledge graph files.
    - [App 2](App-2-KB/) with the populated knowledge base, extended with SWRL rules and knowledge graph files.
- The files complementing 5G Core Network use cases, based on [Free5GC](https://github.com/free5gc/free5gc-compose/blob/d04baa57a6e4c9a2c4af8a223bad984299d100b7/docker-compose.yaml) and [OAI Basic 5G](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-fed/-/blob/94ecfac7476114f730e1b555779a20b3e78d77f0/docker-compose/docker-compose-basic-nrf.yaml), are available at:
    - [Free5GC](Free5GC-KB/) with the populated knowledge base, extended with SWRL rules and knowledge graph files.
    - [OAI5GC](OAI5GC-KB/) with the populated knowledge base, extended with SWRL rules and knowledge graph files.

- The core of the parsing script responsible for the creation of knowledge bases (Data Parsing and Populating Module) and the script used for knowledge graphs creation can be found [here](Scripts/). 


## Contact details 

This project has been created by Aleksandra Simić.
Feel free to reach out if you have any questions, feedback, or collaboration opportunities related to this thesis project:

- Email: aleksandra.simic@ntnu.no