# Postmortem Report: The Great Flash Sale Fiasco

## Introduction
Any software system will eventually fail, and that failure can stem from a wide range of possible factors:
- Bugs
- Traffic spikes
- Security issues
- Hardware failures
- Natural disasters
- Human error

Failing is normal and actually a great opportunity to learn and improve. Any great Software Engineer must learn from their mistakes to ensure they won’t happen again. Failing is fine, but failing twice because of the same issue is not.

A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has two main goals:
1. To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
2. To ensure that the root cause(s) of the outage have been discovered and that measures are taken to make sure it will be fixed.

## Issue Summary
**Duration of Outage:**
- Start: June 18, 2024, 3:00 PM UTC
- End: June 18, 2024, 5:30 PM UTC

**Impact:**
- Service affected: E-commerce Web Application
- Users affected: Approximately 60% of users experienced slow response times and errors when trying to access the website.
- User experience: Users faced slow page loads, frequent timeouts, and inability to complete purchases.

**Root Cause:**
- A sudden spike in traffic due to a flash sale caused the database to become overwhelmed, leading to slow response times and server errors.

## Timeline
- **3:00 PM:** Issue detected. Monitoring alert triggered due to high response times and error rates.
- **3:05 PM:** On-call engineer notified and begins investigation.
- **3:10 PM:** Initial assumption: Server resource (CPU/RAM) overload based on monitoring metrics.
- **3:20 PM:** Misleading path: Restarted web servers, but issue persisted.
- **3:30 PM:** Incident escalated to the database team.
- **3:45 PM:** Database team identifies high query load causing database to slow down.
- **4:00 PM:** Applied temporary rate-limiting on the API to reduce load.
- **4:15 PM:** Optimized database queries and added indexes to improve performance.
- **4:45 PM:** Services begin to stabilize; users gradually regain access.
- **5:30 PM:** Full resolution confirmed, all services operational.

## Root Cause and Resolution
**Root Cause:**
- The e-commerce web application experienced a sudden spike in traffic due to a flash sale. This led to an overload of the database as inefficient queries were unable to handle the increased load effectively.

**Resolution:**
- The database server was restarted to clear the overload.
- Temporary rate-limiting was applied to the API to manage the traffic.
- Database queries were optimized and indexes were added to improve performance.
- Server resources were increased to handle higher traffic volumes in the future.

## Corrective and Preventative Measures
**Improvements and Fixes:**
1. **Database Optimization:** Optimize all database queries and ensure indexes are used efficiently.
2. **Infrastructure Scaling:** Upgrade server resources and implement auto-scaling to handle traffic spikes.
3. **Monitoring and Alerts:** Enhance monitoring to include detailed database performance metrics and set up alerts for unusual traffic patterns.
4. **Code Review and Testing:** Conduct regular code reviews and implement stress testing to ensure system resilience under high load.

**Action Items:**
1. **Optimize Database Queries:** Review and optimize all existing queries in the database.
2. **Upgrade Server Resources:** Increase CPU and RAM for the server and set up auto-scaling.
3. **Implement Advanced Monitoring:**
   - Set up monitoring for database performance metrics.
   - Configure alerts for traffic spikes and resource usage.
4. **Conduct Stress Testing:** Implement regular stress testing to simulate high traffic conditions and ensure the system can handle them.
5. **Review Code:** Conduct a thorough code review to identify and fix potential performance issues.
6. **Update Documentation:** Document all changes made and update runbooks for handling similar incidents in the future.

