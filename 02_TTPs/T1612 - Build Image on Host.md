# Build Image on Host

## Description

Adversaries may build a container image directly on a host to bypass defenses that monitor for the retrieval of malicious images from a public registry. A remote build request may be sent to the Docker API that includes a Dockerfile that pulls a vanilla base image, such as alpine, from a public or local registry and then builds a custom image upon it. [1]

An adversary may take advantage of that build API to build a custom image on the host that includes malware downloaded from their C2 server, and then they may utilize Deploy Container using that custom image. [2] [3] If the base image is pulled from a public registry, defenses will likely not detect the image as malicious since it’s a vanilla image. If the base image already resides in a local registry, the pull may be considered even less suspicious since the image is already in the environment.

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1047 | Audit | Audit images deployed within the environment to ensure they do not contain any malicious components. |
| M1035 | Limit Access to Resource Over Network | Limit communications with the container service to local Unix sockets or remote access via SSH. Require secure port access to communicate with the APIs over TLS by disabling unauthenticated access to the Docker API on port 2375. Instead, communicate with the Docker API over TLS on port 2376. [4] |
| M1030 | Network Segmentation | Deny direct remote access to internal systems through the use of network proxies, gateways, and firewalls. |
| M1026 | Privileged Account Management | Ensure containers are not running as root by default. In Kubernetes environments, consider defining Pod Security Standards that prevent pods from running privileged containers. [5] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0459 | Detection Strategy for Build Image on Host | AN1261 | Detection of container image build activity directly on the host using Docker or Kubernetes APIs. Defenders may observe Docker build requests, anomalous Dockerfile instructions (such as downloading code from unknown IPs), or creation of new images followed by immediate deployment. This behavior chain typically consists of an unexpected image creation event correlated with outbound network communication to non-standard or untrusted destinations. |

---

## References

- [Docker. ( null). Docker Engine API v1.41 Reference - Build an Image. Retrieved March 30, 2021.](https://docs.docker.com/engine/api/v1.41/#operation/ImageBuild)
- [Assaf Morag. (2020, July 15). Threat Alert: Attackers Building Malicious Images on Your Hosts. Retrieved March 29, 2021.](https://blog.aquasec.com/malicious-container-image-docker-container-host)
- [Team Nautilus. (2021, June). Attacks in the Wild on the Container Supply Chain and Infrastructure. Retrieved August 26, 2021.](https://info.aquasec.com/hubfs/Threat%20reports/AquaSecurity_Cloud_Native_Threat_Report_2021.pdf?utm_campaign=WP%20-%20Jun2021%20Nautilus%202021%20Threat%20Research%20Report&utm_medium=email&_hsmi=132931006&_hsenc=p2ANqtz-_8oopT5Uhqab8B7kE0l3iFo1koirxtyfTehxF7N-EdGYrwk30gfiwp5SiNlW3G0TNKZxUcDkYOtwQ9S6nNVNyEO-Dgrw&utm_content=132931006&utm_source=hs_automation)
- [Docker. (n.d.). Protect the Docker Daemon Socket. Retrieved March 29, 2021.](https://docs.docker.com/engine/security/protect-access/)
- [National Security Agency, Cybersecurity and Infrastructure Security Agency. (2022, March). Kubernetes Hardening Guide. Retrieved April 1, 2022.](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)

---
