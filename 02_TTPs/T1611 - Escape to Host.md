# Escape to Host

## Description

Adversaries may break out of a container or virtualized environment to gain access to the underlying host. This can allow an adversary access to other containerized or virtualized resources from the host level or to the host itself. In principle, containerized / virtualized resources should provide a clear separation of application functionality and be isolated from the host environment. [1]

There are multiple ways an adversary may escape from a container to a host environment. Examples include creating a container configured to mount the host’s filesystem using the bind parameter, which allows the adversary to drop payloads and execute control utilities such as cron on the host; utilizing a privileged container to run commands or load a malicious kernel module on the underlying host; or abusing system calls such as unshare and keyctl to escalate privileges and steal secrets. [2] [3] [4] [5] [6] [7]

Additionally, an adversary may be able to exploit a compromised container with a mounted container management socket, such as docker.sock , to break out of the container via a Container Administration Command . [5] Adversaries may also escape via Exploitation for Privilege Escalation , such as exploiting vulnerabilities in global symbolic links in order to access the root directory of a host machine. [8]

In ESXi environments, an adversary may exploit a vulnerability in order to escape from a virtual machine into the hypervisor. [9]

Gaining access to the host may provide the adversary with the opportunity to achieve follow-on objectives, such as establishing persistence, moving laterally within the environment, accessing other containers or virtual machines running on the host, or setting up a command and control channel on the host.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0600 | Doki | Doki ’s container was configured to bind the host root directory. [4] |
| S0601 | Hildegard | Hildegard has used the BOtB tool that can break out of containers. [10] |
| S0683 | Peirates | Peirates can gain a reverse shell on a host node by mounting the Kubernetes hostPath. [11] |
| S0623 | Siloscape | Siloscape maps the host’s C drive to the container by creating a global symbolic link to the host through the calling of NtSetInformationSymbolicLink . [12] |
| G0139 | TeamTNT | TeamTNT has deployed privileged containers that mount the filesystem of victim machine. [13] [14] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1048 | Application Isolation and Sandboxing | Consider utilizing seccomp, seccomp-bpf, or a similar solution that restricts certain system calls such as mount. In Kubernetes environments, consider defining Pod Security Standards that limit container access to host process namespaces, the host network, and the host file system. [15] |
| M1042 | Disable or Remove Feature or Program | Remove unnecessary tools and software from containers. |
| M1038 | Execution Prevention | Use read-only containers, read-only file systems, and minimal images when possible to prevent the running of commands. [15] Where possible, also consider using application control and software restriction tools (such as those provided by SELinux) to restrict access to files, processes, and system calls in containers. [16] |
| M1026 | Privileged Account Management | Ensure containers are not running as root by default and do not use unnecessary privileges or mounted components. In Kubernetes environments, consider defining Pod Security Standards that prevent pods from running privileged containers. [15] |
| M1051 | Update Software | Ensure that hosts are kept up-to-date with security patches. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0219 | Detection Strategy for Escape to Host | AN0612 | Detection of container escape attempts via bind mounts, privileged containers, or abuse of docker.sock. Defenders may observe anomalous volume mount configurations (e.g., hostPath to / or /proc), unexpected privileged container launches, or use of container administration commands to access host resources. These events typically correlate with subsequent process execution on the host outside of normal container isolation. |
| AN0613 | Detection of Linux container escape attempts via syscalls ( unshare , keyctl , mount ) or process execution outside container namespaces. Defenders may correlate unusual system calls from containerized processes with subsequent process creation on the host or modification of host resources. |  |  |
| AN0614 | Detection of Windows container escape attempts by observing processes accessing host directories, symbolic link abuse, or privilege escalation attempts. Defenders may detect anomalous process execution with access to system-level directories outside of container boundaries. |  |  |
| AN0615 | Detection of ESXi escape attempts by monitoring for anomalies in hypervisor logs such as unexpected VM operations, privilege escalation events, or attempts to load malicious kernel modules within the hypervisor environment. |  |  |

---

## References

- [Docker. (n.d.). Docker Overview. Retrieved March 30, 2021.](https://docs.docker.com/get-started/overview/)
- [Docker. (n.d.). Use Bind Mounts. Retrieved March 30, 2021.](https://docs.docker.com/storage/bind-mounts/)
- [Fiser, D., Oliveira, A.. (2019, December 20). Why a Privileged Container in Docker is a Bad Idea. Retrieved March 30, 2021.](https://www.trendmicro.com/en_us/research/19/l/why-running-a-privileged-container-in-docker-is-a-bad-idea.html)
- [Fishbein, N., Kajiloti, M.. (2020, July 28). Watch Your Containers: Doki Infecting Docker Servers in the Cloud. Retrieved March 30, 2021.](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)
- [0xn3va. (n.d.). Escaping. Retrieved May 27, 2022.](https://0xn3va.gitbook.io/cheat-sheets/container/escaping)
- [Manoj Ahuje. (2022, January 31). CVE-2022-0185: Kubernetes Container Escape Using Linux Kernel Exploit. Retrieved July 6, 2022.](https://www.crowdstrike.com/blog/cve-2022-0185-kubernetes-container-escape-using-linux-kernel-exploit/)
- [Mark Manning. (2020, July 23). Keyctl-unmask: "Going Florida" on The State Of Containerizing Linux Keyrings. Retrieved July 6, 2022.](https://www.antitree.com/2020/07/keyctl-unmask-going-florida-on-the-state-of-containerizing-linux-keyrings/)
- [Daniel Prizmant. (2020, July 15). Windows Server Containers Are Open, and Here's How You Can Break Out. Retrieved October 1, 2021.](https://unit42.paloaltonetworks.com/windows-server-containers-vulnerabilities/)
- [Broadcom. (2025, March 6). VMSA-2025-0004: Questions & Answers. Retrieved March 26, 2025.](https://github.com/vmware/vcf-security-and-compliance-guidelines/tree/main/security-advisories/vmsa-2025-0004)
- [Chen, J. et al. (2021, February 3). Hildegard: New TeamTNT Cryptojacking Malware Targeting Kubernetes. Retrieved April 5, 2021.](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
- [InGuardians. (2022, January 5). Peirates GitHub. Retrieved February 8, 2022.](https://github.com/inguardians/peirates)
- [Prizmant, D. (2021, June 7). Siloscape: First Known Malware Targeting Windows Containers to Compromise Cloud Environments. Retrieved June 9, 2021.](https://unit42.paloaltonetworks.com/siloscape/)
- [Fishbein, N. (2020, September 8). Attackers Abusing Legitimate Cloud Monitoring Tools to Conduct Cyber Attacks. Retrieved September 22, 2021.](https://www.intezer.com/blog/cloud-security/attackers-abusing-legitimate-cloud-monitoring-tools-to-conduct-cyber-attacks/)
- [Kol, Roi. Morag, A. (2020, August 25). Deep Analysis of TeamTNT Techniques Using Container Images to Attack. Retrieved September 22, 2021.](https://blog.aquasec.com/container-security-tnt-container-attack)
- [National Security Agency, Cybersecurity and Infrastructure Security Agency. (2022, March). Kubernetes Hardening Guide. Retrieved April 1, 2022.](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)
- [Kubernetes. (n.d.). Configure a Security Context for a Pod or Container. Retrieved March 8, 2023.](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)

---
