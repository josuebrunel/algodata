# Important things to know

## How to approach

### Scoping

1. Functional requirements

2. Non Functional requirements

* Scalability:
    - Understand what kind of users we're handling, troughpot
    - throughpot
    - storage capacity

* performance:
    - latency
    - availability: number of error requests divided (/) by the number of total requests

3. Back of the envelope calculation

* *throughpot* you divide the *number of operation by the number of seconds in a day (86400)*

* latency: https://colin-scott.github.io/personal_website/research/interactive_latency.html


## Desing requirement

1. Move data
2. Store data
3. Transform data

What makes a good system desing:

1. Availability:
    - reliability
    - fault torerent
    - redundancy

2. Throughput:
    - requests/second: user interaction with service
    - query/second (QPS):

3. Latency: how long each request take.

## API Paradigms

1. REST (Representation State Transfer)

It's stateless, it means we need to send everything we know (context/environment) in each request
rEST mainly use JSON as a data format

2. GraphQL

It fixes the overfetching problem face by REST apis. The client is only returned the data that it needs.
Single request to fetch multiple resources
It only has 2 types of requests:
- Querying: fetching data
- Mutation: creation, edition and deletion

One of the downside of GraphQL is caching. We can't cache request as effeciently as REST requests

3. gRPC

It is mainly used for server to server communication and use protobuf as a data format serialized into a binary format

## API Design


## Caching

Caching is used to speed things up

Strategies:

1. Write-around cache : write on disk/storage then populate cache on reading
2. Write-through cache: write on cache then on disk
3. Write-back cache: write on cache and periodicaly populate disk

Eviction policy:

1. FIFO: First In First Out
2. LRU: Least Recently Used
3. LFU: Least Frequently Used


## Content Delivery Network (CDN)

Just as cache, it's to speed things up. Moving data closer to the user is faster

## Proxies

- Forward proxy, protect the client from the outside world. They can be used to control outward trafic
- Reverse proyx, protect the server from the outside world. They can be used to control inward trafic

1. Load Balancer

They are used to balance the inward traffic. There are several strategis to balance the inward trafic:
* Round Robin: 1st request hit 1st server, 2nd request hit 2nd server, ... full cycle
* Round Robin Weighted: it's like round robin but the first with the highest weight handle the most requests
* Location: we serve request according to the location of the server
* consistant hashing


## Storage

### RDBMS

They are **acid** compliant. It means they guarantee:
- Atomicity: every db transaction is all or nothing ( atomic )
- Consistency: prevent inconsistent state
- Isolation: serialize, executed in a particular order to avoid dirty read or write
- Durability

### NoSQL

Their main advantage is scalability
There are several type of NoSQL db:
- Key/Value store
- Document Store: no schema
- Wide column database: mainly used for heavy writing. Good when reading and updating are not important (Cassandra, Big Table)
- Graph: used for heavy relationship models

### Replication and sharding

Replication helps with scaling. There several strategies for replication:
- leader / follower: the write on the leader and replicate data (asycn/sync) into the follower. The downside might be a slight inconsistency
- leader / leader: write and read are on done on all leaders. The downsides are inconsistency and latency

When replication is not enough, we can use sharding to help.
Sharding is about evenly dividing data on different hosts

### CAP Theory (Consistency, Availability, Partition Tolerance)

It only applies to replicated database. In a nustshell it is a simple logic problem:
If nodes can't communicate with each other we can't both guarantee **Consistency and Availability**.
An extension to the CAP theorem is the **PACELC** which means:
```
if P {
    choose A or C
} esle {
    favor Latency or Consistency
}
```

### Object storage

It mainly used to store large blob (Binary Large Object) or for long term storage

### Big Data

1. Message Queues

They are mainly used to process event asynchronously. There might more than one producer and more than one consumer.

A Pub/Sub model can be used to process events. Events processing are done by **topic**.
Events in a topic can be processed by multiiple **subscribers**

2. MapReduce

It's about processing very big data. There are generally 2 ways to process big data:
- Batch: data is given upfront then processed
- Streaming:






