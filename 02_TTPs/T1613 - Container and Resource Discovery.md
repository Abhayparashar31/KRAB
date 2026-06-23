# Container and Resource Discovery

## Description

Adversaries may attempt to discover containers and other resources that are available within a containers environment. Other resources may include images, deployments, pods, nodes, and other information such as the status of a cluster.

These resources can be viewed within web applications such as the Kubernetes dashboard or can be queried via the Docker and Kubernetes APIs. [1] [2] In Docker, logs may leak information about the environment, such as the environment’s configuration, which services are available, and what cloud provider the victim may be utilizing. The discovery of these resources may inform an adversary’s next steps in the environment, such as how to perform lateral movement and which methods to utilize for execution.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0601 | Hildegard | Hildegard has used masscan to search for kubelets and the kubelet API for additional running containers. [3] |
| S0683 | Peirates | Peirates can enumerate Kubernetes pods in a given namespace. [4] |
| G0139 | TeamTNT | TeamTNT has checked for running containers with docker ps and for specific container names with docker inspect . [5] TeamTNT has also searched for Kubernetes pods running in a local network. [6] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1035 | Limit Access to Resource Over Network | Limit communications with the container service to managed and secured channels, such as local Unix sockets or remote access via SSH. Require secure port access to communicate with the APIs over TLS by disabling unauthenticated access to the Docker API and Kubernetes API Server. [7] [8] In Kubernetes clusters deployed in cloud environments, use native cloud platform features to restrict the IP ranges that are permitted to access to API server. [9] Where possible, consider enabling just-in-time (JIT) access to the Kubernetes API to place additional restrictions on access. [10] |
| M1030 | Network Segmentation | Deny direct remote access to internal systems through the use of network proxies, gateways, and firewalls. |
| M1018 | User Account Management | Enforce the principle of least privilege by limiting dashboard visibility to only the required users. When using Kubernetes, avoid giving users wildcard permissions or adding users to the system:masters group, and use RoleBindings rather than ClusterRoleBindings to limit user privileges to specific namespaces. [11] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0490 | Detection Strategy for Container and Resource Discovery | AN1352 | Detection of adversary attempts to enumerate containers, pods, nodes, and related resources within containerized environments. Defenders may observe anomalous API calls to Docker or Kubernetes (e.g., 'docker ps', 'kubectl get pods', 'kubectl get nodes'), unusual account activity against the Kubernetes dashboard, or unexpected queries against container metadata endpoints. These events should be correlated with user context and network activity to reveal resource discovery attempts. |

---

## References

- [Docker. (n.d.). Docker Engine API v1.41 Reference. Retrieved March 31, 2021.](https://docs.docker.com/engine/api/v1.41/)
- [The Kubernetes Authors. (n.d.). The Kubernetes API. Retrieved March 29, 2021.](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)
- [Chen, J. et al. (2021, February 3). Hildegard: New TeamTNT Cryptojacking Malware Targeting Kubernetes. Retrieved April 5, 2021.](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
- [InGuardians. (2022, January 5). Peirates GitHub. Retrieved February 8, 2022.](https://github.com/inguardians/peirates)
- [Fiser, D. Oliveira, A. (n.d.). Tracking the Activities of TeamTNT A Closer Look at a Cloud-Focused Malicious Actor Group. Retrieved September 22, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-tracking-the-activities-of-teamTNT.pdf)
- [Darin Smith. (2022, April 21). TeamTNT targeting AWS, Alibaba. Retrieved August 4, 2022.](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)
- [Docker. (n.d.). Protect the Docker Daemon Socket. Retrieved March 29, 2021.](https://docs.docker.com/engine/security/protect-access/)
- [The Kubernetes Authors. (n.d.). Controlling Access to The Kubernetes API. Retrieved March 29, 2021.](https://kubernetes.io/docs/concepts/security/controlling-access/)
- [Kubernetes. (n.d.). Overview of Cloud Native Security. Retrieved March 8, 2023.](https://kubernetes.io/docs/concepts/security/overview/)
- [Microsoft. (2023, February 27). AKS-managed Azure Active Directory integration. Retrieved March 8, 2023.](https://learn.microsoft.com/en-us/azure/aks/managed-aad)
- [Kubernetes. (n.d.). Role Based Access Control Good Practices. Retrieved March 8, 2023.](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)

---
