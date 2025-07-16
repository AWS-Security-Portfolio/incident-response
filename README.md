## AWS Incident Response & Automated Quarantine Lab

Implemented real-time threat detection and automated response in AWS using GuardDuty, CloudTrail, and Lambda to detect, investigate, and isolate EC2 security incidents.

---

## Table of Contents

- [Overview]
- [Diagram]
- [Objectives]
- [Steps Performed]
  - [1. GuardDuty Enablement]
  - [2. CloudTrail Setup]
  - [3. EC2 Attack Simulation]
  - [4. Lambda Quarantine Automation]
  - [5. Documentation & Reflection]
- [Screenshots & Deliverables]
- [Lessons Learned]
- [References]

--- 

## Overview

This lab demonstrates AWS incident response and automation capabilities by simulating a port scan attack against an EC2 instance, detecting the event with GuardDuty, investigating with CloudTrail, and automatically quarantining the affected EC2 using a Lambda function. The workflow closely resembles real-world cloud security operations and highlights the importance of detection, investigation, containment, and documentation.

---

## Diagram

![Incident Response Lab Diagram](Diagram.png)

---

## Objectives

- Enable GuardDuty for continuous threat detection on AWS resources.
- Set up CloudTrail for multi-region API activity logging.
- Launch and configure an EC2 test instance.
- Simulate a security incident (port scan) and/or inject a GuardDuty sample finding.
- Analyze incident evidence using CloudTrail logs.
- Build and deploy a Lambda function to automatically quarantine the affected EC2 instance.
- Document all steps, findings, and automation with screenshots and reflections.

---

## Steps Performed

1. GuardDuty Enablement
   - Enabled GuardDuty in the target AWS region.
   - Confirmed GuardDuty was active and ready to generate findings.

2. CloudTrail Setup
   - Created a multi-region CloudTrail trail for API and security event logging.
   - Configured an S3 bucket for log storage.

3. EC2 Attack Simulation
   - Launched a test EC2 instance with SSH open to the internet.
   - Simulated a port scan attack using nmap from an external host.
   - When no finding appeared, generated a sample GuardDuty finding via AWS CLI.

4. Lambda Quarantine Automation
   - Developed a Python Lambda function to create and assign a quarantine security group to the affected EC2 instance.
   - Attached required EC2 permissions to the Lambda execution role.
   - Tested Lambda function and verified network isolation of the instance.

5. Documentation & Reflection
   - Collected all relevant screenshots for each step.
   - Created a comprehensive playbook and timeline.
   - Added a personal reflection on lessons learned and future automation improvements.

---

## Screenshots & Deliverables

*All screenshots are included in the screenshots/ folder.

| Order | File Name                                 | What it Shows                                        |
|-------|-------------------------------------------|------------------------------------------------------|
| 1     | GuardDuty-Enabled.png                     | GuardDuty enabled in AWS Console                     |
| 2     | CloudTrail-TrailCreated.png               | CloudTrail multi-region trail created                |
| 3     | CloudTrail-EventHistory.png               | CloudTrail event history review                      |
| 4     | EC2-Instance-Running.png                  | EC2 test instance running                            |
| 5     | EC2-SecurityGroup-SSH-Open.png            | Security group with SSH open                         |
| 6     | GuardDuty-Simulated-PortProbe-Finding.png | Simulated GuardDuty finding                          |
| 7     | Lambda-Code.png                           | Lambda quarantine function code                      |
| 8     | Lambda-Permissions.png                    | Lambda execution role permissions                    |
| 9     | Lambda-Quarantine-TestSuccess.png         | Lambda success output: instance quarantined          |
| 10    | EC2-Quarantined-SecurityGroup.png         | EC2 attached to quarantine security group            |
| 11    | QuarantineSG-NoInboundRules.png           | Quarantine security group: no inbound rules          |

## Screenshot Explanations

1. GuardDuty-Enabled.png: Enabled GuardDuty in the AWS Console to provide real-time threat detection across all resources in the selected region. This step is essential for receiving security findings and automating incident response.

2. CloudTrail-TrailCreated.png: Created a multi-region CloudTrail trail and configured log delivery to a dedicated S3 bucket. This ensures all API activity and security events are captured for auditing and investigation.

3. CloudTrail-EventHistory.png: Reviewed CloudTrail event history to verify logging and provide evidence of API events, including the simulation of a security incident and its detection.

4. EC2-Instance-Running.png: Launched an EC2 instance for testing incident detection and response. This screenshot confirms the instance was running and available for the lab.

5. EC2-SecurityGroup-SSH-Open.png: Configured a Security Group to allow SSH (port 22) from any IP address. This configuration enabled the simulation of a port scan and demonstrated potential exposure.

6. GuardDuty-Simulated-PortProbe-Finding.png: Simulated a GuardDuty finding for a port probe reconnaissance event. This shows GuardDuty’s ability to detect suspicious network activity, even when triggered by sample data.

7. Lambda-Code.png: Developed a Python Lambda function that automatically creates and attaches a quarantine security group to an EC2 instance under investigation. The code enforces network isolation as a containment step.

8. Lambda-Permissions.png: Attached the necessary IAM permissions (AmazonEC2FullAccess and AWSLambdaBasicExecutionRole) to the Lambda execution role, enabling it to manage EC2 security groups and instances securely.

9. Lambda-Quarantine-TestSuccess.png: Successfully ran the Lambda function to quarantine the target EC2 instance. The output confirms the operation completed as expected.

10. EC2-Quarantined-SecurityGroup.png: Verified that the EC2 instance is now attached only to the quarantine security group, effectively cutting off all inbound network access.

11. QuarantineSG-NoInboundRules.png: Reviewed the quarantine security group settings to confirm it has no inbound rules, providing proof that the instance is fully isolated from external traffic.

---

## Lessons Learned

- GuardDuty and CloudTrail together provide strong detection and audit capabilities for AWS environments.
- Automating incident response with Lambda enables rapid containment of threats.
- Documentation with detailed screenshots and stepwise playbooks is key for both audits and career portfolios.
- Simulated findings and automation pipelines are invaluable when working in sandbox or free-tier AWS environments.

---

## References

- AWS GuardDuty Documentation
  https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html

- AWS CloudTrail Documentation
  https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html

- AWS Lambda Documentation
  https://docs.aws.amazon.com/lambda/latest/dg/welcome.html

- AWS Security Best Practices
  https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-controls-reference.html

---

Sebastian Silva C. – July 2025 – Berlin, Germany
