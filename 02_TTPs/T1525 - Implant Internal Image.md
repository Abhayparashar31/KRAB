# Implant Internal Image

## Description

Adversaries may implant cloud or container images with malicious code to establish persistence after gaining access to an environment. Amazon Web Services (AWS) Amazon Machine Images (AMIs), Google Cloud Platform (GCP) Images, and Azure Images as well as popular container runtimes such as Docker can be implanted or backdoored. Unlike Upload Malware , this technique focuses on adversaries implanting an image in a registry within a victim’s environment. Depending on how the infrastructure is provisioned, this could provide persistent access if the infrastructure provisioning tool is instructed to always use the latest image. [1]

A tool has been developed to facilitate planting backdoors in cloud container images. [2] If an adversary has access to a compromised AWS instance, and permissions to list the available container images, they may implant a backdoor such as a Web Shell . [1]

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1047 | Audit | Periodically check the integrity of images and containers used in cloud deployments to ensure they have not been modified to include malicious software. |
| M1045 | Code Signing | Several cloud service providers support content trust models that require container images be signed by trusted sources. [3] [4] |
| M1026 | Privileged Account Management | Limit permissions associated with creating and modifying platform images or containers based on the principle of least privilege. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0334 | Detection Strategy for T1525 – Implant Internal Image | AN0946 | Implantation of malicious code into container images followed by registry push and use in new deployments. |
| AN0947 | Creation or modification of cloud virtual machine images (AMIs, custom images) with persistence mechanisms, followed by infrastructure provisioning that uses these implanted images. |  |  |

---

## References

- [Rhino Labs. (2019, August). Exploiting AWS ECR and ECS with the Cloud Container Attack Tool (CCAT). Retrieved September 12, 2019.](https://rhinosecuritylabs.com/aws/cloud-container-attack-tool/)
- [Rhino Labs. (2019, September). Cloud Container Attack Tool (CCAT). Retrieved September 12, 2019.](https://github.com/RhinoSecurityLabs/ccat)
- [Microsoft. (2019, September 5). Content trust in Azure Container Registry. Retrieved October 16, 2019.](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)
- [Docker. (2019, October 10). Content trust in Docker. Retrieved October 16, 2019.](https://docs.docker.com/engine/security/trust/content_trust/)

---
