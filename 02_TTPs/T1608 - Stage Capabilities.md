# Stage Capabilities

## Description

Adversaries may upload, install, or otherwise set up capabilities that can be used during targeting. To support their operations, an adversary may need to take capabilities they developed ( Develop Capabilities ) or obtained ( Obtain Capabilities ) and stage them on infrastructure under their control. These capabilities may be staged on infrastructure that was previously purchased/rented by the adversary ( Acquire Infrastructure ) or was otherwise compromised by them ( Compromise Infrastructure ). Capabilities may also be staged on web services, such as GitHub or Pastebin, or on Platform-as-a-Service (PaaS) offerings that enable users to easily provision applications. [1] [2] [3] [4] [5]

Staging of capabilities can aid the adversary in a number of initial access and post-compromise behaviors, including (but not limited to):

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0129 | Mustang Panda | Mustang Panda has used servers under their control to validate tracking pixels sent to phishing victims. [12] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1056 | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0839 | Detection of Stage Capabilities | AN1971 | If infrastructure or patterns in malware, tooling, certificates, or malicious web content have been previously identified, internet scanning may uncover when an adversary has staged their capabilities. Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on related stages of the adversary lifecycle, such as initial access and post-compromise behaviors. |

---

## References

- [Adair, S. and Lancaster, T. (2020, November 6). OceanLotus: Extending Cyber Espionage Operations Through Fake Websites. Retrieved November 20, 2020.](https://www.volexity.com/blog/2020/11/06/oceanlotus-extending-cyber-espionage-operations-through-fake-websites/)
- [Kent Backman. (2021, May 18). When Intrusions Don’t Align: A New Water Watering Hole and Oldsmar. Retrieved August 18, 2022.](https://www.dragos.com/blog/industry-news/a-new-water-watering-hole/)
- [Jérôme Segura. (2019, December 4). There's an app for that: web skimmers found on PaaS Heroku. Retrieved August 18, 2022.](https://www.malwarebytes.com/blog/news/2019/12/theres-an-app-for-that-web-skimmers-found-on-paas-heroku)
- [Ashwin Vamshi. (2019, January 24). Targeted Attacks Abusing Google Cloud Platform Open Redirection. Retrieved August 18, 2022.](https://www.netskope.com/blog/targeted-attacks-abusing-google-cloud-platform-open-redirection)
- [Ashwin Vamshi. (2020, August 12). A Big Catch: Cloud Phishing from Google App Engine and Azure App Service. Retrieved August 18, 2022.](https://www.netskope.com/blog/a-big-catch-cloud-phishing-from-google-app-engine-and-azure-app-service)
- [Kindlund, D. (2012, December 30). CFR Watering Hole Attack Details. Retrieved November 17, 2024.](https://web.archive.org/web/20201024230407/https://www.fireeye.com/blog/threat-research/2012/12/council-foreign-relations-water-hole-attack-details.html)
- [Gallagher, S.. (2015, August 5). Newly discovered Chinese hacking group hacked 100+ websites to use as “watering holes”. Retrieved January 25, 2016.](http://arstechnica.com/security/2015/08/newly-discovered-chinese-hacking-group-hacked-100-websites-to-use-as-watering-holes/)
- [Blasco, J. (2014, August 28). Scanbox: A Reconnaissance Framework Used with Watering Hole Attacks. Retrieved October 19, 2020.](https://cybersecurity.att.com/blogs/labs-research/scanbox-a-reconnaissance-framework-used-on-watering-hole-attacks)
- [Malwarebytes Threat Intelligence Team. (2020, October 14). Silent Librarian APT right on schedule for 20/21 academic year. Retrieved February 3, 2021.](https://blog.malwarebytes.com/malwarebytes-news/2020/10/silent-librarian-apt-phishing-attack/)
- [Proofpoint Threat Insight Team. (2019, September 5). Threat Actor Profile: TA407, the Silent Librarian. Retrieved February 3, 2021.](https://www.proofpoint.com/us/threat-insight/post/threat-actor-profile-ta407-silent-librarian)
- [DigiCert. (n.d.). How to Install an SSL Certificate. Retrieved April 19, 2021.](https://www.digicert.com/kb/ssl-certificate-installation.htm)
- [Raggi, M. et al. (2022, March 7). The Good, the Bad, and the Web Bug: TA416 Increases Operational Tempo Against European Governments as Conflict in Ukraine Escalates. Retrieved March 16, 2022.](https://www.proofpoint.com/us/blog/threat-insight/good-bad-and-web-bug-ta416-increases-operational-tempo-against-european)

---
