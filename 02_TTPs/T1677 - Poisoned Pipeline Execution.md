# Poisoned Pipeline Execution

## Description

Adversaries may manipulate continuous integration / continuous development (CI/CD) processes by injecting malicious code into the build process. There are several mechanisms for poisoning pipelines:

By poisoning CI/CD pipelines, threat actors may be able to gain access to credentials, laterally move to additional hosts, or input malicious components to be shipped further down the pipeline (i.e., Supply Chain Compromise ).

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S9008 | Shai-Hulud | Shai-Hulud has also leveraged GitHub actions from stolen accounts in order to create a malicious Github workflow within .github/workflows/discussion.yaml . [8] [9] [10] [11] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1054 | Software Configuration | Where possible, avoid allowing pipelines to run unreviewed code. Where this is necessary, ensure that these pipelines are executed on isolated nodes without access to secrets. In GitHub, avoid using the pull_request_target trigger if possible, do not treat user-controlled inputs (such as branch names) as trusted, and do not use self-hosted runners on public repositories. |
| M1018 | User Account Management | Ensure that CI/CD pipelines only have permissions they require to complete their operations. Additionally, limit the number of users who have write access to internal repositories to only those necessary. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0533 | Detection Strategy for Poisoned Pipeline Execution via SaaS CI/CD Workflows | AN1473 | Detects anomalous CI/CD workflow execution originating from forked repositories, with pull request (PR) metadata or commit messages containing suspicious patterns (e.g., encoded payloads), coupled with the use of insecure pipeline triggers like pull_request_target or excessive API usage of CI/CD secrets. Correlation with unusual artifact generation or secret exfiltration via encoded or external network destination URLs confirms suspicious behavior. |

---

## References

- [Omer Gilm Aviad Hahami, Asi Greenholts, and Yaron Avital. (2025, March 20). GitHub Actions Supply Chain Attack: A Targeted Attack on Coinbase Expanded to the Widespread tj-actions/changed-files Incident: Threat Assessment . Retrieved May 22, 2025.](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)
- [OWASP. (n.d.). CICD-SEC-4: Poisoned Pipeline Execution (PPE). Retrieved May 22, 2025.](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-04-Poisoned-Pipeline-Execution)
- [Jaroslav Lobačevski. (2021, August 3). Keeping your GitHub Actions and workflows secure Part 1: Preventing pwn requests. Retrieved May 22, 2025.](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/)
- [Wiz Threat Research. (2024, December 9). Ultralytics AI Library Hacked via GitHub for Cryptomining. Retrieved May 22, 2025.](https://www.wiz.io/blog/ultralytics-ai-library-hacked-via-github-for-cryptomining)
- [Hugo Vincent. (2024, May 22). Hijacking GitHub runners to compromise the organization. Retrieved May 22, 2025.](https://www.synacktiv.com/en/publications/hijacking-github-runners-to-compromise-the-organization)
- [Jaroslav Lobačevski. (2021, August 4). Keeping your GitHub Actions and workflows secure Part 2: Untrusted input. Retrieved May 22, 2025.](https://securitylab.github.com/resources/github-actions-untrusted-input/)
- [John Stawinski IV. (2024, January 11). Playing with Fire – How We Executed a Critical Supply Chain Attack on PyTorch. Retrieved May 22, 2025.](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/)
- [Charlie Eriksen. (2025, September 16). S1ngularity/nx attackers strike again. Retrieved April 9, 2026.](https://www.aikido.dev/blog/s1ngularity-nx-attackers-strike-again)
- [Gianpietro Cutolo. (2025, November 26). Shai-Hulud 2.0: Aggressive, Automated, and Fast Spreading. Retrieved April 9, 2026.](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)
- [Justin Moore. (2025, November 25). "Shai-Hulud" Worm Compromises npm Ecosystem in Supply Chain Attack (Updated November 26). Retrieved April 9, 2026.](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/)
- [Socket Research Team. (2025, November 24). Shai Hulud Strikes Again (v2). Retrieved April 9, 2026.](https://socket.dev/blog/shai-hulud-strikes-again-v2)

---
