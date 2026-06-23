# Container Administration Command

## Description

Adversaries may abuse a container administration service to execute commands within a container. A container administration service such as the Docker daemon, the Kubernetes API server, or the kubelet may allow remote management of containers within an environment. [1] [2] [3]

In Docker, adversaries may specify an entrypoint during container deployment that executes a script or command, or they may use a command such as docker exec to execute a command within a running container. [4] [5] In Kubernetes, if an adversary has sufficient permissions, they may gain remote execution in a container in the cluster via interaction with the Kubernetes API server, the kubelet, or by running a command such as kubectl exec . [6]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0601 | Hildegard | Hildegard was executed through the kubelet API run command and by executing commands on running containers. [7] |
| S0599 | Kinsing | Kinsing was executed with an Ubuntu container entry point that runs shell scripts. [8] |
| S0683 | Peirates | Peirates can use kubectl or the Kubernetes API to run commands. [9] |
| S0623 | Siloscape | Siloscape can send kubectl commands to victim clusters through an IRC channel and can run kubectl locally to spread once within a victim cluster. [10] |
| G0139 | TeamTNT | TeamTNT executed Hildegard through the kubelet API run command and by executing commands on running containers. [7] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1042 | Disable or Remove Feature or Program | Remove unnecessary tools and software from containers. |
| M1038 | Execution Prevention | Use read-only containers, read-only file systems, and minimal images when possible to prevent the execution of commands. [11] Where possible, also consider using application control and software restriction tools (such as those provided by SELinux) to restrict access to files, processes, and system calls in containers. [12] |
| M1035 | Limit Access to Resource Over Network | Limit communications with the container service to managed and secured channels, such as local Unix sockets or remote access via SSH. Require secure port access to communicate with the APIs over TLS by disabling unauthenticated access to the Docker API and Kubernetes API Server. [13] [14] In Kubernetes clusters deployed in cloud environments, use native cloud platform features to restrict the IP ranges that are permitted to access to API server. [15] Where possible, consider enabling just-in-time (JIT) access to the Kubernetes API to place additional restrictions on access. [16] |
| M1026 | Privileged Account Management | Ensure containers are not running as root by default. In Kubernetes environments, consider defining Pod Security Standards that prevent pods from running privileged containers and using the NodeRestriction admission controller to deny the kublet access to nodes and pods outside of the node it belongs to. [11] [17] |
| M1018 | User Account Management | Enforce authentication and role-based access control on the container service to restrict users to the least privileges required. [11] When using Kubernetes, avoid giving users wildcard permissions or adding users to the system:masters group, and use RoleBindings rather than ClusterRoleBindings to limit user privileges to specific namespaces. [18] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0065 | Detection Strategy for Container Administration Command Abuse | AN0177 | Defenders may detect abuse of container administration commands by observing anomalous use of management utilities ( docker exec , kubectl exec , or API calls to kubelet) correlated with unexpected process creation inside containers. Behavioral chains include unauthorized API requests followed by command execution within running pods or containers, often originating from unusual user accounts, automation scripts, or IP addresses outside the expected cluster management plane. |

---

## References

- [Docker. (n.d.). DockerD CLI. Retrieved March 29, 2021.](https://docs.docker.com/engine/reference/commandline/dockerd/)
- [The Kubernetes Authors. (n.d.). The Kubernetes API. Retrieved March 29, 2021.](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)
- [The Kubernetes Authors. (n.d.). Kubelet. Retrieved March 29, 2021.](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)
- [Docker. (n.d.). Docker run reference. Retrieved March 29, 2021.](https://docs.docker.com/engine/reference/run/#entrypoint-default-command-to-execute-at-runtime)
- [Docker. (n.d.). Docker Exec. Retrieved March 29, 2021.](https://docs.docker.com/engine/reference/commandline/exec/)
- [The Kubernetes Authors. (n.d.). Get a Shell to a Running Container. Retrieved March 29, 2021.](https://kubernetes.io/docs/tasks/debug-application-cluster/get-shell-running-container/)
- [Chen, J. et al. (2021, February 3). Hildegard: New TeamTNT Cryptojacking Malware Targeting Kubernetes. Retrieved April 5, 2021.](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
- [Singer, G. (2020, April 3). Threat Alert: Kinsing Malware Attacks Targeting Container Environments. Retrieved April 1, 2021.](https://blog.aquasec.com/threat-alert-kinsing-malware-container-vulnerability)
- [InGuardians. (2022, January 5). Peirates GitHub. Retrieved February 8, 2022.](https://github.com/inguardians/peirates)
- [Prizmant, D. (2021, June 7). Siloscape: First Known Malware Targeting Windows Containers to Compromise Cloud Environments. Retrieved June 9, 2021.](https://unit42.paloaltonetworks.com/siloscape/)
- [National Security Agency, Cybersecurity and Infrastructure Security Agency. (2022, March). Kubernetes Hardening Guide. Retrieved April 1, 2022.](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)
- [Kubernetes. (n.d.). Configure a Security Context for a Pod or Container. Retrieved March 8, 2023.](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
- [Docker. (n.d.). Protect the Docker Daemon Socket. Retrieved March 29, 2021.](https://docs.docker.com/engine/security/protect-access/)
- [The Kubernetes Authors. (n.d.). Controlling Access to The Kubernetes API. Retrieved March 29, 2021.](https://kubernetes.io/docs/concepts/security/controlling-access/)
- [Kubernetes. (n.d.). Overview of Cloud Native Security. Retrieved March 8, 2023.](https://kubernetes.io/docs/concepts/security/overview/)
- [Microsoft. (2023, February 27). AKS-managed Azure Active Directory integration. Retrieved March 8, 2023.](https://learn.microsoft.com/en-us/azure/aks/managed-aad)
- [Kubernetes. (n.d.). Admission Controllers Reference. Retrieved March 8, 2023.](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)
- [Kubernetes. (n.d.). Role Based Access Control Good Practices. Retrieved March 8, 2023.](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)

---
