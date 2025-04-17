""""
Hypothetically, we are building an app that collects accelerometer data from thin clients
(sensors with limited processing capacity)

a. Assuming that the device is sending continuously at 16000Hz for the X,Y, and Z
acceleration measurements, what would your strategy be in handling and
processing the data? How would you design the server infrastructure? Please
enumerate the steps, software, algorithms, and services that you would use to
ensure that the servers can handle the incoming data from our users. Diagrams
can be really helpful for this.


16,000 Hz means 16,000 samples (sets of X, Y, and Z values) are taken per second.

for each sample is one reading of X, Y, and Z value

For example, at time t=0.0001s, the sensor might say: X = 0.5, Y = -0.3, Z = 0.8

This is 1 sample


"""


"""
how i calculate the how many second the sensor get 

seconds = number of samples/samples rate
16,000 number of samples/16,000 sampling rate = 1 seconds

thats actually quite large data to send to the server

whats more if those sensors send a real time data per 10ms if 16000 sample for 1 second

10 ms = 10 / 1,000 = 0.01 seconds.

Samples in 10 ms = Sampling Rate x Time (in seconds)
16,000 x 0.01 = 160 samples


So, sending these data points every 10 ms would result in an extremely high volume of network traffic.

"""


"""
1. Using Cloud Run to Create an API Server
Cloud Run has a built-in load balancer, so when you deploy your API server there, Google automatically manages the traffic for you.

- Make sure to set a minimum number of instances in Cloud Run to keep your API server always ready, even when there's low traffic. This helps avoid cold starts, ensuring faster response times when requests come in. 
- consider the availability and capacity of the selected region. Opting for regions with higher resource availability can help maintain performance during traffic spikes and prevent potential service disruptions due to resource limitations.
However, this is optional if you're utilizing multi-region load balancing, as Cloud Run can handle traffic distribution across regions automatically.
- Consider configuring the concurrency setting in Cloud Run to control how many requests each instance can handle simultaneously. 
    for example 1000 request per second / 10 concurrent = can create 100 instances
    if every request has 16000 Hz/Samples, 10 concurrent is enough to handle the traffic per second if not the instances will scale beyong 100 instances

2. Using Multi Region Load Balancer
- Cloud Run's built-in load balancer operates within a single region. If that region experiences high traffic or becomes unavailable, your API server might become unreachable. 
Implementing a multi-region load balancer can help distribute traffic across multiple regions, ensuring your API remains accessible even if one region faces issues.

3. use Monitoring system
- creating custom dashboard in under monitoring can help visualize metrics such as traffic volume, CPU usage, memory allocation, and instance count. 
it helps in tracking the health and performance of our API Server.
- create custom alert to identify the potential bottlenecks of our server for example i would create an alert to check if the instances exceed in a certain threshold or errors in the API Server

4.  Background Processing via Pub/Sub
- If each request sends something heavy, like request with a 1600 sampling rate, the API server might slow down or even time out. So instead, I publish the data to Pub/Sub and let a background Cloud Run worker handle the processing. 
It keeps the API fast and lets the system scale automatically kind of like using Celery, but serverless. Unlike Celery, which needs a running worker process, it's not ideal for Cloud Run since instances shut down when idle. 
Pub/Sub works better here because it automatically triggers a new Cloud Run instance to handle the task whenever a message is published.

Optional:

5. we could 

"""

